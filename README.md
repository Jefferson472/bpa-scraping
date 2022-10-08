# Task BPA - Scraping

## Escopo do Projeto
O escopo do teste se baseia em abrir o site da Amazon, pesquisar por  iPhone (com busca apenas por web scraping), pegar os resultados da primeira página (nome e preço) e criar uma planilha Excel com esses dados (transcrever o nome e valor do produto).

---

## Requirements
- Python 3.10

---

## Executando o Projeto
Para executar o projeto siga os passos abaixo:

1. Instale as dependências do projeto:

    ```pip install -r requirements.txt```

2. Execute o comando para inicializar a coleta de dados:

    ```python .\src\main.py```

3. Serão exibidas algumas informações no console e ao final o arquivo `amazon-iphone-list.csv` com os dados estará disponível na raiz do projeto.