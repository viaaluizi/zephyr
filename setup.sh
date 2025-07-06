#!/bin/bash
# Cria ambiente virtual
python3 -m venv venv

# Ativa o ambiente virtual
source venv/bin/activate

# Instala as dependências
pip install -r requirements.txt

# Cria o arquivo .env com placeholder
echo 'API_TOKEN="seu_token_aqui"' > .env

echo "✅ Ambiente configurado. Edite o arquivo .env com seu token da API."
