from pymongo import MongoClient
from gridfs import GridFS
from bson import SON

def getKapsuleLocus(bacteria_name):
    # Conectar ao MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["teste2"]
    collection = db["Bacteria"]
    fs = GridFS(db)

    # Buscar o documento no MongoDB
    documento = collection.find_one({f"{bacteria_name}.tools.kleborate": {"$exists": True}})

    if not documento:
        print("Nenhum documento encontrado para essa bactéria.")
        return None

    # Obter o file_id do documento
    file_info = documento.get(bacteria_name, {}).get("tools", {}).get("kleborate", {}).get(f"{bacteria_name}.txt")
    
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

    # Verificar se a coluna "klebsiella_pneumo_complex__kaptive__K_locus" existe
    try:
        indice_k_locus = colunas.index("klebsiella_pneumo_complex__kaptive__K_locus")
    except ValueError:
        print("Coluna 'klebsiella_pneumo_complex__kaptive__K_locus' não encontrada no arquivo.")
        return None

    # Obter o valor correspondente à bactéria
    dados = linhas[1].split("\t")
    kapsule_locus = dados[indice_k_locus] if len(dados) > indice_k_locus else None

    return kapsule_locus

