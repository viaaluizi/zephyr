import os
from dotenv import load_dotenv
import pandas as pd
import requests
import time
import logging

# Configuração dos logs
logging.basicConfig(
    level=logging.INFO,  # Configura o nível de log para INFO
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato dos logs
    handlers=[
        logging.FileHandler("zephyr_logs.log"),  # Salva os logs em um arquivo
        logging.StreamHandler()  # Adiciona um handler para exibir logs no console
    ]
)

# CONFIGURAÇÕES DO USUÁRIO

# Substitua pelos valores reais da sua instância Zephyr
base_url = "https://api.zephyrscale.smartbear.com/v2"
load_dotenv()
api_token = os.getenv("API_TOKEN")
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Nome do arquivo Excel com os cenários
excel_file = "cenarios_teste.xlsx"

# FUNÇÕES AUXILIARES

def create_payload(row):
    return {
        "name": row["name"],
        "projectKey": row["projectKey"],
        "folderId": int(row["folderId"]) if pd.notna(row["folderId"]) else None,
        "priority": row["priority"],
        "statusName": row["status"],
        "objective": row["objective"],
        "precondition": row["precondition"],
        "componentId": int(row["componentId"])if pd.notna(row["componentId"]) else None,
        "labels": row["labels"].split(",") if pd.notna(row["labels"]) else []
    }

# 1ª LEITURA: CRIAR CENÁRIOS

# Carrega o Excel com os dados dos cenários
df = pd.read_excel(excel_file, engine="openpyxl")

required_columns = ["name", "projectKey", "folderId", "priority", "status", "objective", "precondition", "componentId", "labels", "bdd"]
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    raise ValueError(f"Falta informações importantes no seu arquivo, valide as colunas do seu arquivo excel {missing_columns}")

# Dicionário para mapear nome do cenário para sua chave (key) retornada pela API
cenario_key_map = {}

for _, row in df.iterrows():
    # Monta o payload para criação do cenário
    test_case_payload = create_payload(row)

    # Requisição para criar o cenário
    response = requests.post(f"{base_url}/testcases", headers=headers, json=test_case_payload)

    if response.status_code == 201:
        test_case = response.json()
        test_case_key = test_case["key"]
        cenario_key_map[row["name"]] = test_case_key
        logging.info(f"Cenário '{row['name']}' criado com sucesso! com a key: {test_case_key}")
    elif response.status_code != 200:
        logging.error(
            f"Falha ao criar cenário '{row['name']}': {response.status_code}. Response: {response.text}"
        )

    # Pausa de 1 segundo entre requisições
    time.sleep(1)

# 2ª LEITURA: ADICIONAR SCRIPT BDD

# Lê o Excel
df = pd.read_excel(excel_file, engine="openpyxl")

for _, row in df.iterrows():
    nome_cenario = row["name"]
    test_case_key = cenario_key_map.get(nome_cenario)

    if not test_case_key:
        logging.warning(f"Cenário '{nome_cenario}' não foi criado. Pulando script BDD.")
        continue

    # Limpa o conteúdo BDD (remove aspas extras e espaços)
    bdd = str(row["bdd"]).replace("\\n", "\n").replace('"', '').strip()

    # Payload para adicionar script BDD
    bdd_payload = {
        "type": "bdd",
        "text": bdd
    }

    # Requisição para adicionar script BDD
    bdd_response = requests.post(
        f"{base_url}/testcases/{test_case_key}/testscript",
        headers=headers,
        json=bdd_payload
    )
    time.sleep(1)

    if bdd_response.status_code in [200, 201]:
        logging.info(f"Script BDD adicionado ao cenário com sucesso '{nome_cenario}'")
    else:
        logging.error(
            f"Falha ao adicionar script BDD ao cenário '{nome_cenario}': {bdd_response.status_code}. Response: {bdd_response.text}"
        )

