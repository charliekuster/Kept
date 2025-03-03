import paramiko
from pymongo import MongoClient
from gridfs import GridFS
import stat

# Configurações do servidor
host = "kp.unifesp.br"
port = 9004  
username = "charlie"
password = "Ch4r1i3@Kept"
remote_path = "/home/data/analysis/LNCC_ok"

# Criar um cliente SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Criar um cliente Mongo
client = MongoClient("mongodb://localhost:27017/")
db = client["teste2"]
collection = db["Bacteria"]
fs = GridFS(db)  # Criar um GridFS para armazenar arquivos grandes

def insert_collection(path):
    """Essa função insere documentos no MongoDB com estrutura aninhada, sem filtro de prefixo"""
    print(f"Acessando o caminho: {path}")
    
    try:
        items = sftp.listdir_attr(path)
        item_data = {}  # Dicionário para armazenar estrutura hierárquica

        for item in items:
            item_path = f"{path}/{item.filename}"
            print(f"Analisando: {item.filename}")

            if stat.S_ISDIR(item.st_mode):  # Se for diretório, chama recursivamente
                print(f"Encontrado diretório: {item.filename}. Processando recursivamente...")
                item_data[item.filename] = insert_collection(item_path)
            else:
                # Para arquivos, adiciona ao dicionário
                print(f"Encontrado arquivo: {item.filename}")
                
                file_data = {
                    "path": item_path,
                    "name": item.filename
                }

                # Salva o arquivo no GridFS e pega o ID
                file_id = upload_file(item_path, item.filename)
                if file_id:
                    file_data["file_id"] = file_id  # Armazena o ID do arquivo no GridFS
                    print(f"Arquivo {item.filename} inserido no GridFS com ID: {file_id}")
                else:
                    print(f"Erro ao inserir arquivo {item.filename} no GridFS.")

                item_data[item.filename] = file_data

        return item_data  # Retorna a estrutura completa do diretório
    except Exception as e:
        print(f"Erro ao acessar {path}: {e}")
        return {}

def upload_file(file_path, file_name):
    """Lê um arquivo via SFTP e armazena no GridFS"""
    print(f"Iniciando o upload do arquivo {file_name} para o GridFS...")
    try:
        with sftp.open(file_path, 'rb') as file_stream:
            file_id = fs.put(file_stream, filename=file_name)
            print(f"Arquivo {file_name} carregado com sucesso. ID do arquivo: {file_id}")
            return file_id
    except Exception as e:
        print(f"Erro ao fazer upload do arquivo {file_name}: {e}")
        return None

def insert_bacteria_collection():
    """Insere todos os arquivos de cada bactéria de forma aninhada no MongoDB"""
    bacteria_path = remote_path
    print(f"Iniciando inserção das pastas das bactérias a partir do caminho: {bacteria_path}")
    
    try:
        # Lista todas as pastas de bactérias
        bacteria_folders = sftp.listdir_attr(bacteria_path)
        
        for bacteria in bacteria_folders:
            if stat.S_ISDIR(bacteria.st_mode):  # Verifica se é um diretório
                bacteria_name = bacteria.filename
                bacteria_path_full = f"{bacteria_path}/{bacteria_name}"
                print(f"Processando bactéria: {bacteria_name}")
                
                # Chama a função recursiva para preencher a estrutura da bactéria
                bacteria_data = insert_collection(bacteria_path_full)
                print(f"Estrutura hierárquica da bactéria {bacteria_name} criada com sucesso.")
                
                # Insere os dados da bactéria na coleção
                collection.insert_one({bacteria_name: bacteria_data})
                print(f"Dados da bactéria {bacteria_name} inseridos na coleção MongoDB.")

    except Exception as e:
        print(f"Erro ao inserir bactérias na coleção: {e}")

try:
    # Conectar ao servidor
    print("Conectando ao servidor SSH...")
    ssh.connect(host, port, username, password)
    print("Conexão SSH bem-sucedida!")

    # Criar um cliente SFTP 
    sftp = ssh.open_sftp()

    # Inserir dados das bactérias
    insert_bacteria_collection()

    # Fechar conexões
    sftp.close()
    ssh.close()
    print("Conexões SSH e SFTP fechadas.")

except Exception as e:
    print(f"Erro ao conectar ao servidor ou durante o processo: {e}")