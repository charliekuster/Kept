from fastapi import APIRouter, Depends, HTTPException
from pymongo.database import Database as MongoDatabase
from pymongo.collection import Collection
from bson import ObjectId
from backend.services.database import get_db

router = APIRouter(
    prefix="/klebsiela",
    tags=["klebsiela"]
)

@router.get("/bacteria/ids")
def get_bacteria_ids(db: MongoDatabase = Depends(get_db)):
    """
    Retorna uma lista de IDs dos documentos na coleção 'Bacteria'.
    """
    collection: Collection = db["Bacteria"]
    
    # Busca todos os documentos e projeta apenas o campo _id
    documents = collection.find({}, {"_id": 1})
    
    # Converte os ObjectIds para strings e os adiciona a uma lista
    ids_list = [str(doc["_id"]) for doc in documents]
    
    return {"ids": ids_list}

def extract_paths(data, paths_list):
    """ Função recursiva para extrair todas as rotas dos arquivos. """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "path":
                paths_list.append(value)
            else:
                extract_paths(value, paths_list)
    elif isinstance(data, list):
        for item in data:
            extract_paths(item, paths_list)

@router.get("/bacteria/paths")
def get_bacteria_paths(db: MongoDatabase = Depends(get_db)):
    """
    Retorna todas as rotas dos arquivos armazenados no banco de dados.
    """
    collection: Collection = db["Bacteria"]
    
    paths_list = []
    for document in collection.find({}, {"_id": 0}):  # Ignora o _id
        extract_paths(document, paths_list)  # Chama a função recursiva

    return {"paths": paths_list}

@router.get("/bacteria/{id}")
def get_bacteria_by_id(id: str, db: MongoDatabase = Depends(get_db)):
    """
    Busca um documento específico no banco de dados pelo seu ObjectId.
    """
    collection: Collection = db["Bacteria"]
    
    try:
        object_id = ObjectId(id)  # Converte para ObjectId
    except:
        raise HTTPException(status_code=400, detail="ID inválido")
    paths_list = []
    document = collection.find_one({"_id": object_id})
    
    if not document:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    extract_paths(document, paths_list)   
    return {"paths": paths_list}

