# Aplicação de Análise de Ações

Esta é uma aplicação Django para análise de dados e notícias sobre ações. A aplicação utiliza Celery para tarefas em segundo plano e Redis para gerenciamento de mensagens.

## Funcionalidades

- Autenticação e registro de usuários
- Operações CRUD para ações
- Tarefas em segundo plano para buscar notícias sobre ações e atualizar a análise de sentimento

## Pré-requisitos

- [Docker](https://www.docker.com/products/docker-desktop)

## Começando

### Atraso na Configuração Inicial

Observe que, na primeira vez que você inicializar o projeto, pode demorar um pouco para que as ações e as notícias sejam processadas. Esse atraso ocorre devido ao tempo de resposta da API Finbert, que pode ser lento. Além disso, a aplicação busca dados de ações e artigos de notícias em segundo plano usando tarefas Celery, e esse processo também pode levar algum tempo para ser concluído inicialmente.

### Clonar o Repositório

```sh
git clone https://github.com/yourusername/stock_analysis.git
cd stock_analysis
```

### Configuração do Docker

1. **Construir e executar os contêineres:**

    ```sh
    docker compose up --build
    ```

2. **Executar as migrações do banco de dados:**

    O `command` especificado no arquivo `docker-compose.yml` executará automaticamente as migrações e iniciará o servidor Django.

3. **Acessar a aplicação:**

    Abra o navegador e vá para `http://localhost:8000`.

## Tecnologias

- Django
- Celery
- Redis
- Docker
