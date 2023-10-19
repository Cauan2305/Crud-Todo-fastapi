# FastAPI TODO App API

## Descrição do Projeto

Este é um projeto de API desenvolvido em Python com o framework FastAPI e utilizando um banco de dados MongoDB. A API foi criada para um aplicativo de lista de tarefas (TODO) e permite a criação, leitura, atualização e exclusão de tarefas. Além disso, oferece funcionalidades adicionais, como a marcação de tarefas como concluídas e a busca por tarefas com base em diferentes critérios.

## Requisitos

Antes de executar a API, certifique-se de que você possui o seguinte software instalado:

- Python 3.7 ou superior
- FastAPI
- MongoDB

Recomenda-se a criação de um ambiente virtual Python para isolar as dependências do projeto. Você pode criar um ambiente virtual usando o seguinte comando:

```bash
python -m venv venv
```

Em seguida, ative o ambiente virtual:

- No Windows:

```bash
venv\Scripts\activate
```

- No macOS e Linux:

```bash
source venv/bin/activate
```

Instale as dependências do projeto usando o `pip`:

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

Antes de usar a API, você deve configurar o MongoDB. Certifique-se de ter o MongoDB instalado e em execução na sua máquina. A configuração do banco de dados pode ser ajustada no arquivo `config.py`.

```python
MONGODB_URL = "mongodb://localhost:27017/"
```

Certifique-se de alterar a URL e o nome do banco de dados de acordo com suas configurações.

## Executando a API

Para iniciar a API, execute o seguinte comando a partir do diretório raiz do projeto:

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`. Você pode acessar a documentação interativa da API em `http://localhost:8000/docs` e a interface alternativa em `http://localhost:8000/redoc`.

Certifique-se de usar um cliente HTTP, como o [httpie](https://httpie.io/) ou [curl](https://curl.se/), para interagir com a API.


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para criar problemas (issues) e enviar solicitações de pull (pull requests) para melhorar o projeto.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

---

Divirta-se usando a API de lista de tarefas FastAPI! Se você tiver alguma dúvida ou precisar de ajuda, não hesite em entrar em contato.

**Equipe do FastAPI TODO App API**