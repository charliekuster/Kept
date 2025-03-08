from fastapi import APIRouter, Depends, HTTPException
from pymongo.database import Database as MongoDatabase
from pymongo.collection import Collection
from fastapi.responses import FileResponse
from bson import ObjectId
from backend.services.database import get_db
from gridfs import GridFS
import tempfile

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
    Busca um documento específico no banco de dados pelo seu ObjectId e retorna
    as rotas dos arquivos junto com seus respectivos file_id.
    """
    collection: Collection = db["Bacteria"]
    
    try:
        object_id = ObjectId(id)  # Converte para ObjectId
    except:
        raise HTTPException(status_code=400, detail="ID inválido")
    
    document = collection.find_one({"_id": object_id})
    
    if not document:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    
    def extract_paths_and_ids(data, result_list):
        """Função recursiva para extrair todas as rotas dos arquivos e seus file_id."""
        if isinstance(data, dict):
            path = data.get("path")
            file_id = data.get("file_id")
            if path and file_id:
                result_list.append({"path": path, "file_id": str(file_id)})
            for value in data.values():
                extract_paths_and_ids(value, result_list)
        elif isinstance(data, list):
            for item in data:
                extract_paths_and_ids(item, result_list)
    
    result_list = []
    extract_paths_and_ids(document, result_list)
    
    return {"files": result_list}


###################

@router.get("/download/{file_id}")
def download_file(file_id: str, db: MongoDatabase = Depends(get_db)):
    """
    Faz o download de um arquivo armazenado no GridFS pelo seu file_id.
    """
    try:
        # Conectar ao GridFS
        fs = GridFS(db)

        # Converter file_id para ObjectId
        object_id = ObjectId(file_id)

        # Recuperar o arquivo do GridFS
        arquivo = fs.get(object_id)

        # Criar um arquivo temporário
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(arquivo.read())
        temp_file.close()

        # Retornar o arquivo para download
        return FileResponse(temp_file.name, filename=arquivo.filename, media_type="application/octet-stream")

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Arquivo não encontrado: {str(e)}")
