from pymongo import MongoClient
from gridfs import GridFS
from bson import SON


# Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Selecionar o banco de dados
db = client['teste2']

# Selecionar a coleção
collection = db['Bacteria']

# Inicializar o GridFS
fs = GridFS(db)

# Consultar o documento

documento = (collection.find_one({"KSP33.main.qc.summary": {"$exists": True}})).get("KSP33", {}).get("main", {}).get("qc", {}).get("summary", SON())

if documento:
    valor = documento.get("KSP33_R1-final_fastqc.html")
    #print(valor)
    # Extrair o file_id
    file_id = valor.get("file_id")
    print(file_id)
    
    # Converter o file_id para ObjectId
    from bson import ObjectId
    file_id = ObjectId(file_id)
    
    # Recuperar o arquivo do GridFS
    arquivo = fs.get(file_id)
    print(arquivo)
    # Ler o conteúdo do arquivo
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:", conteudo)
else:
    print("Nenhum documento encontrado.")