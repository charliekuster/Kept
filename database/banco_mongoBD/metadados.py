import pandas as pd
from pymongo import MongoClient
from getKL import getKapsuleLocus
from getCapb import getCarbapenemResistance
from getFasta import getFastaFileId

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["teste2"]
collection = db["Bacteria"]

# Carregar a planilha para um DataFrame
file_path = "banco_mongoBD/tabeladados.xlsx"  # Substituir pelo caminho real
df = pd.read_excel(file_path, header=None)  

# Ajustar o cabeçalho corretamente
df.iloc[0] = df.iloc[0].ffill(axis=0)  # Preenche os valores mesclados horizontalmente
df.columns = df.iloc[1]  # Define a segunda linha como cabeçalho
df = df[2:].reset_index(drop=True)  # Remove as duas primeiras linhas e reseta os índices

# Atualizar os documentos existentes no MongoDB
for _, row in df.iterrows():
    bacteria_name = row["ID"] # Certifique-se de que a coluna ID corresponde ao nome das bactérias
    if isinstance(bacteria_name, float) or str(bacteria_name).lower() == "nan" or not bacteria_name:
        continue
    metadados = row.to_dict()

    # Adicionando os novos campos
    metadados["Organism"] = "Klebsiella pneumoniae"
    metadados["Annotation method"] = "Prokka"
    metadados["Kapsule Locus"] = getKapsuleLocus(bacteria_name)
    metadados["Carbapenem resistance"] = getCarbapenemResistance(bacteria_name)
    metadados["Fasta"] = getFastaFileId(bacteria_name)

    # Atualizar o campo correspondente dentro do documento
    result = collection.update_one(
        {bacteria_name: {"$exists": True}},  # Busca o documento que contém a bactéria
        {"$set": {f"{bacteria_name}.metadados": metadados}},  # Atualiza ou adiciona os metadados
        upsert=False  # Não cria um novo documento se não existir
    )

    if result.matched_count > 0:
        print(f"Metadados atualizados para {bacteria_name}")
        
    else:
        print(f"Bactéria {bacteria_name} não encontrada no MongoDB")

print("Atualização concluída!")


