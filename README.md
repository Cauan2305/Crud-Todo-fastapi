# FastAPI TODO App API

## Descrição do Projeto

Este é um projeto de API desenvolvido em Python com o framework FastAPI e utilizando um banco de dados MongoDB. A API foi criada para um aplicativo de lista de tarefas (TODO) e permite a criação, leitura, atualização e exclusão de tarefas. Além disso, oferece funcionalidades adicionais, como a marcação de tarefas como concluídas e a busca por tarefas com base em diferentes critérios.

## Requisitos

Antes de executar a API, certifique-se de que você possui o seguinte software instalado:

- Python 3.7 ou superior
- FastAPI
- MongoDB
- Docker

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

## Executando a API com Docker

Você pode executar este projeto utilizando Docker, o que facilita a configuração do ambiente de desenvolvimento. Certifique-se de ter o Docker instalado em sua máquina.

1. Clone o repositório do projeto:

```bash
git clone https://github.com/Cauan2305/Crud-Todo-fastapi.git
```

2. Navegue até o diretório do projeto:

```bash
cd nomedoseuprojeto
```

3. Crie uma imagem Docker a partir do Dockerfile incluído no projeto. Substitua "nomedocontainer" pelo nome que você deseja para o contêiner e "versao" pela versão desejada.

```bash
docker build -t nomedocontainer:versao .
```

4. Inicie um contêiner Docker a partir da imagem que você criou. Substitua "nomedocontainer" e "versao" pelos mesmos valores usados na etapa anterior.

```bash
docker run -d -p 8000:80 nomedocontainer:versao
```

Agora, a API FastAPI TODO App estará em execução dentro do contêiner Docker. Você pode acessá-la em `http://localhost:8000`.

Para parar o contêiner Docker, você pode listar os contêineres em execução:

```bash
docker ps
```

Em seguida, pare o contêiner com o comando `docker stop CONTAINER_ID`, onde `CONTAINER_ID` é o ID do contêiner listado.

Lembre-se de que, para interagir com a API, você ainda pode usar um cliente HTTP, como o [httpie](https://httpie.io/) ou [curl](https://curl.se/), conforme mencionado na seção original. Contribuições são bem-vindas e boa sorte com o seu projeto!

Se você tiver alguma dúvida ou precisar de ajuda adicional, não hesite em entrar em contato.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para criar problemas (issues) e enviar solicitações de pull (pull requests) para melhorar o projeto.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

---

Divirta-se usando a API de lista de tarefas FastAPI! Se você tiver alguma dúvida ou precisar de ajuda, não hesite em entrar em contato.

**Equipe do FastAPI TODO App API**