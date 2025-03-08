from pymongo import MongoClient
from gridfs import GridFS

def getGBKFileId(bacteria_name):
    # Conectar ao MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["teste2"]
    collection = db["Bacteria"]
    fs = GridFS(db)

    #.gbk = main/annotator/prokka/*.gbk.gz
    # Buscar o documento no MongoDB
    documento = collection.find_one({f"{bacteria_name}.main.annotator.prokka": {"$exists": True}})

    if not documento:
        print("Nenhum documento encontrado para essa bactéria.")
        return None

    # Obter o file_id do arquivo .fna.gz
    file_info = documento.get(bacteria_name, {}).get("main", {}).get("annotator", {}).get("prokka", {}).get(f"{bacteria_name}.gbk.gz")

    if not file_info or "file_id" not in file_info:
        print("Arquivo não encontrado no GridFS.")
        return None

    # Garantir que o file_id seja único e em formato de string
    file_ids = {str(file_info["file_id"])}  # Usando set para evitar duplicados
    
    return list(file_ids)[0]  
