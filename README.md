# API-CRUD
# API CRUD de Produtos com FastAPI, Docker, SQLAlchemy e MongoDB

Este projeto fornece uma API CRUD de produtos com logging de visualizações em MongoDB. Construído com FastAPI e Docker para um ambiente de desenvolvimento e execução isolado, oferece um CRUD completo, documentado e seguro.

## Tecnologias Utilizadas

- **FastAPI**: Framework Python para criação de APIs RESTful.
- **Docker**: Gerenciamento de contêineres para garantir um ambiente isolado e consistente.
- **SQLAlchemy** e **SQLite**: Armazenamento de dados relacionais e mapeamento objeto-relacional.
- **MongoDB**: Armazenamento dos logs de visualizações de produtos.
- **Alembic**: Migrações de banco de dados.
- **Pydantic**: Validação de dados de entrada.
- **Postman**: Documentação e testes das rotas da API.

## Funcionalidades Principais

- **CRUD de Produtos**: Operações para gerenciar os produtos no banco de dados relacional.
- **Logs de Visualização**: Logs de acessos e visualizações de produtos são armazenados no MongoDB.
- **Validações e Segurança**: Validações de entrada com Pydantic e práticas de segurança para SQL Injection e XSS.
- **Rate Limiting**: Controle de limite de requisições para evitar sobrecarga.

## Como Executar o Projeto

### Pré-requisitos

- **Docker** e **Docker Compose** instalados.

### Passos para Iniciar

##1 Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/API-CRUD-Produtos.git
   cd API-CRUD-Produtos
Inicie o ambiente com Docker Compose:

bash
Copiar código
docker-compose up -d
Acesse a API:

URL base da API: http://localhost:8000
Documentação interativa: http://localhost:8000/docs
Execute os testes:

Use o Postman para verificar as rotas. Uma coleção com todos os endpoints está incluída no projeto.
Estrutura de Diretórios
app/controllers: Controladores da API, incluindo operações CRUD de produtos.
app/models: Modelos SQLAlchemy que representam as tabelas.
app/database: Configuração do banco de dados e sessão de conexão.
app/mongodb: Configuração e funções de logging no MongoDB.
main.py: Arquivo principal para execução do FastAPI.
Dockerfile e docker-compose.yml: Configurações de contêineres Docker.
Documentação e Testes
Documentação automática: Disponível em /docs, gerada pelo FastAPI com Swagger UI.
Postman Collection: A coleção Postman com as rotas está incluída, documentando cada endpoint e permitindo execução de testes.
Contribuições
Sinta-se à vontade para abrir issues e pull requests no repositório GitHub para melhorias e sugestões.##