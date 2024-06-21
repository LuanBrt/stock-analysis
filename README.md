```markdown
# Aplicação de Análise de Ações

Esta é uma aplicação Django para análise de dados e notícias sobre ações. A aplicação utiliza Celery para tarefas em segundo plano e Redis para gerenciamento de mensagens.

## Funcionalidades

- Autenticação e registro de usuários
- Operações CRUD para ações
- Tarefas em segundo plano para buscar notícias sobre ações e atualizar a análise de sentimento

## Pré-requisitos

- [Docker](https://www.docker.com/products/docker-desktop)
- Docker Compose

## Começando

### Atraso na Configuração Inicial

Observe que, na primeira vez que você inicializar o projeto, pode haver um atraso no processamento das ações e das notícias. Esse atraso é devido ao tempo de resposta da API Finbert, que pode ser lento. Além disso, a aplicação realiza a busca de dados de ações e artigos de notícias em segundo plano usando tarefas Celery, o que pode levar algum tempo para ser concluído inicialmente.

Para monitorar o processamento dos dados, um arquivo de logs do Celery (celery.logs) será criado automaticamente ao iniciar e rodar o projeto. Recomenda-se observar a ação Agilent (código A), pois ela será a primeira a ser processada, permitindo acompanhar o funcionamento do sistema desde o início.

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
