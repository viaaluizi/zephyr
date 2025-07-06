# 🧪 Automação de Cenários de Teste com Zephyr Scale

Este projeto tem como objetivo automatizar a criação de cenários de teste no Zephyr Scale a partir de uma planilha Excel. Ele permite:

- Criar automaticamente os cenários com base nos dados fornecidos.
- Adicionar scripts BDD aos cenários criados.
- Organizar os testes por pastas, componentes e etiquetas.

A automação é feita via API do Zephyr Scale, utilizando Python e bibliotecas como `pandas`, `requests`, `openpyxl` e `dontenv`.

## 🚀 Funcionalidades

- Criação automática de cenários de teste no Zephyr Scale a partir de planilha Excel.
- Adição de scripts BDD aos cenários criados.
- Suporte a múltiplos campos como prioridade, status, labels, componentes, etc.
- Mapeamento de nomes de cenários para suas chaves (keys) retornadas pela API.
- Integração com a API REST do Zephyr Scale.

## Prompt para Geração de Cenários BDD
Este repositório inclui um prompt especializado que facilita a criação de cenários de teste comportamentais (BDD) a partir de documentos de requisitos.
O prompt orienta a análise crítica de regras de negócio e gera automaticamente os cenários no formato Gherkin (Given, When, Then), priorizando os caminhos felizes e regras principais.
Ideal para equipes de QA, produto e desenvolvimento que desejam acelerar a definição de testes com foco em comportamento.
O prompt se encontra no arquivo  `prmpt.txt

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Conta e token de acesso à API do Zephyr Scale
- Estrutura de planilha Excel compatível (`cenarios_teste.xlsx`)
- Dependências listadas no `requirements.txt`:
  - `pandas`
  - `requests`
  - `openpyxl`
  - `python-dotenv`

## 🛠️ Instalação
- Clone este repositório e instale as dependências com:

- Certifique-se de estar usando uma versão do Python 3.8 ou superior.

- 🔐 Configuração do .env
- Crie um arquivo chamado .env na raiz do projeto com o seguinte conteúdo:
- Substitua "seu_token_aqui" pelo seu token de autenticação da API do Zephyr Scale.

- ▶️ Execução
- Para rodar o script e criar os cenários de teste, execute:
- Certifique-se de que o arquivo cenarios_teste.xlsx esteja presente no mesmo diretório e siga a estrutura esperada.

## ⚠️ Erros Comuns
- 1. Erro 401 – Unauthorized
Causa: Token da API inválido ou ausente.
Solução: Verifique se o arquivo .env está presente e contém a variável API_TOKEN corretamente definida.

- 2. Erro 400 – Bad Request
Causa: Dados incorretos ou campos obrigatórios ausentes no Excel.
Solução: Confirme se todos os campos obrigatórios estão preenchidos corretamente na planilha (name, projectKey, folderId, etc.).

- 3. Erro 404 – Not Found
Causa: projectKey, folderId ou componentId inválidos.
Solução: Verifique se os IDs e chaves informados existem no Zephyr Scale.

- 4. Erro ao ler o Excel
Causa: Arquivo cenarios_teste.xlsx não encontrado ou mal formatado.
Solução: Certifique-se de que o arquivo está no mesmo diretório do script e que os nomes das colunas estão corretos.

- 5. Problemas com o script BDD
Causa: Campo bdd vazio ou mal formatado.
Solução: Verifique se o conteúdo do campo bdd está em formato de texto e segue a estrutura esperada (ex: Dado, Quando, Então).

## Scripts para facilitar a execução do projeto no Windows:

- 🛠️ setup.bat — Cria o ambiente virtual, instala as dependências e gera o .env com um placeholder.
- ▶️ run.bat — Ativa o ambiente virtual e executa o script zephyr_modificado.py.
- ✅ Como usar no Windows:
 - Execute o setup.bat com um duplo clique ou via terminal: setup.bat

 - Edite o arquivo .env com seu token da API.

 - Execute o projeto com: run.bat

 ## Scripts para facilitar a execução do projeto no Linux/MacOs:

- 🛠️ setup.sh — Cria o ambiente virtual, instala as dependências e gera o .env com um placeholder.
- ▶️ run.sh — Ativa o ambiente virtual e executa o script zephyr_modificado.py.
- ✅ Como usar no Linux/MacOs:
  - Torne os scripts executáveis (Linux/macOS): chmod +x setup.sh run.sh

  - Configure o ambiente: ./setup.sh

  - Edite o .env com seu token da API.

   - Execute o projeto: ./run.sh




