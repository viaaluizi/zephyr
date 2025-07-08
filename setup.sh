#!/bin/bash
# Cria ambiente virtual
python3 -m venv venv

# Ativa o ambiente virtual
source venv/bin/activate

# Instala as dependências
pip install -r requirements.txt

# Solicita ao usuário o valor da variável de ambiente API_TOKEN
read -p "Digite o valor do API_TOKEN: " API_TOKEN

# Adiciona a variável de ambiente ao arquivo .bashrc ou .zshrc
echo "export API_TOKEN=\"$API_TOKEN\"" >> ~/.bashrc
echo "export API_TOKEN=\"$API_TOKEN\"" >> ~/.zshrc

# Cria o arquivo .env com o valor inserido
echo "API_TOKEN=\"$API_TOKEN\"" > .env

# Exibe mensagem de sucesso
echo "Variável de ambiente API_TOKEN configurada com sucesso!"
echo "Ambiente configurado. Edite o arquivo .env se necessário."

# Finaliza o script
deactivate