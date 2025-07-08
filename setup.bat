@echo off
REM Cria ambiente virtual
python -m venv venv

REM Ativa o ambiente virtual
call venv\Scripts\activate

REM Instala as dependências
pip install -r requirements.txt

REM Solicita ao usuário o valor da variável de ambiente API_TOKEN
set /p API_TOKEN="Digite o valor do API_TOKEN: e pressione Enter:"

REM Verifica se o valor foi inserido
if "%API_TOKEN%"=="" (
    echo ERRO: Você deve inserir um valor para o API_TOKEN!
    pause
    exit /b
)

REM Adiciona a variável de ambiente API_TOKEN
setx API_TOKEN "%API_TOKEN%"

REM Exibe mensagem de sucesso
echo Variavel de ambiente API_TOKEN configurada com sucesso!

REM Cria o arquivo .env com o valor inserido
echo API_TOKEN="%API_TOKEN%" > .env

echo Ambiente configurado. Edite o arquivo .env se necessario.

REM Informa ao usuário para adicionar o arquivo excel no diretório
echo Coloque o arquivo Excel no diretorio atual para que o script possa acessa-lo. O nome do arquivo deve ser "cenarios_teste.xlsx".
echo Apos adicionar o arquivo, execute o script principal com o comando:
echo python zephyr.py ou execute o arquivo run.bat para iniciar o script.
echo.

pause