from pymongo import MongoClient
from gridfs import GridFS

def getCarbapenemResistance(bacteria_name):
    # Conectar ao MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["teste2"]
    collection = db["Bacteria"]
    fs = GridFS(db)

    # Buscar o documento no MongoDB
    documento = collection.find_one({f"{bacteria_name}.tools.amrfinderplus": {"$exists": True}})

    if not documento:
        print("Nenhum documento encontrado para essa bactéria.")
        return None

    # Obter o file_id do documento
    file_info = documento.get(bacteria_name, {}).get("tools", {}).get("amrfinderplus", {}).get(f"{bacteria_name}.tsv")

    if not file_info or "file_id" not in file_info:
        print("Arquivo não encontrado no GridFS.")
        return None
    
    file_id = file_info["file_id"]

    # Recuperar o arquivo do GridFS
    try:
        arquivo = fs.get(file_id)
        conteudo = arquivo.read().decode("utf-8")  # Ler como texto
    except Exception as e:
        print("Erro ao recuperar arquivo:", e)
        return None

    # Processar o conteúdo do arquivo
    linhas = conteudo.split("\n")
    if len(linhas) < 2:
        print("Arquivo não contém dados suficientes.")
        return None

    # Obter os cabeçalhos (nomes das colunas)
    colunas = linhas[0].split("\t")

    # Verificar se as colunas necessárias existem
    try:
        indice_subclass = colunas.index("Subclass")
        indice_name_closest = colunas.index("Name of closest sequence")
    except ValueError:
        print("Colunas 'Subclass' ou 'Name of closest sequence' não encontradas no arquivo.")
        return None

    # Percorrer as linhas para encontrar "CARBAPENEM"
    resistencia = []
    for linha in linhas[1:]:  # Ignora o cabeçalho
        dados = linha.split("\t")
        if len(dados) > max(indice_subclass, indice_name_closest):
            if dados[indice_subclass].upper() == "CARBAPENEM":
                resistencia.append(dados[indice_name_closest])

    return resistencia[0] if resistencia else None


