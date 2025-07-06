import os
from dotenv import load_dotenv
import pandas as pd
import requests
import time

# ============================
# CONFIGURAÇÕES DO USUÁRIO
# ============================

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

# ============================
# 1ª LEITURA: CRIAR CENÁRIOS
# ============================

# Carrega o Excel com os dados dos cenários
df = pd.read_excel(excel_file, engine="openpyxl")

# Dicionário para mapear nome do cenário para sua chave (key) retornada pela API
cenario_key_map = {}

for _, row in df.iterrows():
    # Monta a descrição com objetivo e precondição
    descricao = f"Objetivo: {row['objective']}\nPrecondição: {row['precondition']}"

    # Monta o payload para criação do cenário
    test_case_payload = {
        "name": row["name"],
        "projectKey": row["projectKey"],
        "folderId": int(row["folderId"]),
        "priority": row["priority"],
        "statusName": row["status"],
        "objective": row["objective"],
        "precondition": row["precondition"],
        "componentId": int(row["componentId"]),
        "labels": row["labels"].split(",") if pd.notna(row["labels"]) else []
    }

    # Requisição para criar o cenário
    response = requests.post(f"{base_url}/testcases", headers=headers, json=test_case_payload)

    if response.status_code == 201:
        test_case = response.json()
        test_case_key = test_case["key"]
        cenario_key_map[row["name"]] = test_case_key
        print(f"[OK] Cenário '{row['name']}' criado com key: {test_case_key}")
    else:
        print(f"[ERRO] Falha ao criar cenário '{row['name']}': {response.status_code}")
        print(response.text)

    # Pausa de 1 segundo entre requisições
    time.sleep(1)

# ============================
# 2ª LEITURA: ADICIONAR SCRIPT BDD E LABELS
# ============================

# Lê novamente o Excel
df = pd.read_excel(excel_file, engine="openpyxl")

for _, row in df.iterrows():
    nome_cenario = row["name"]
    test_case_key = cenario_key_map.get(nome_cenario)

    if not test_case_key:
        print(f"[AVISO] Cenário '{nome_cenario}' não foi criado. Pulando script BDD.")
        continue

    # Limpa o conteúdo BDD (remove aspas extras e espaços)
    bdd = str(row["bdd"]).replace("\\n", "\n").replace('"', '').strip()

    # Payload para adicionar script BDD
    bdd_payload = {
        "type": "bdd",
        "text": bdd
    }

    # Exibe o payload BDD para depuração
    # print(bdd_payload)

    # Requisição para adicionar script BDD
    bdd_response = requests.post(
        f"{base_url}/testcases/{test_case_key}/testscript",
        headers=headers,
        json=bdd_payload
    )
    time.sleep(1)

    if bdd_response.status_code in [200, 201]:
        print(f"[OK] Script BDD adicionado ao cenário '{nome_cenario}'")
    else:
        print(f"[ERRO] Falha ao adicionar script BDD ao cenário '{nome_cenario}': {bdd_response.status_code}")
        print(bdd_response.text)

