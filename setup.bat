@echo off
REM Cria ambiente virtual
python -m venv venv

REM Ativa o ambiente virtual
call venv\Scripts\activate

REM Instala as dependências
pip install -r requirements.txt

REM Cria o arquivo .env com placeholder
echo API_TOKEN="seu_token_aqui" > .env

echo Ambiente configurado. Edite o arquivo .env com seu token da API.
pause
