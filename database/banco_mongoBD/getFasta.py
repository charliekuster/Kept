from pymongo import MongoClient
from gridfs import GridFS

def getFastaFileId(bacteria_name):
    # Conectar ao MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["teste2"]
    collection = db["Bacteria"]
    fs = GridFS(db)

    # Buscar o documento no MongoDB
    documento = collection.find_one({f"{bacteria_name}.main.assembler": {"$exists": True}})

    if not documento:
        print("Nenhum documento encontrado para essa bactéria.")
        return None

    # Obter o file_id do arquivo .fna.gz
    file_info = documento.get(bacteria_name, {}).get("main", {}).get("assembler", {}).get(f"{bacteria_name}.fna.gz")

    if not file_info or "file_id" not in file_info:
        print("Arquivo não encontrado no GridFS.")
        return None

    # Garantir que o file_id seja único e em formato de string
    file_ids = {str(file_info["file_id"])}  # Usando set para evitar duplicados
    
    return list(file_ids)[0]  


