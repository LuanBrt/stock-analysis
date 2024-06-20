# Stock Analysis Application

This is a Django application for analyzing stock data and news. The application uses Celery for background tasks and Redis for message brokering.

## Features

- User authentication and registration
- CRUD operations for stocks
- Background tasks for fetching stock news and updating sentiment analysis

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- Docker Compose

## Getting Started

### Clone the Repository

```sh
git clone https://github.com/yourusername/stock_analysis.git
cd stock_analysis
```

### Docker Setup

1. **Build and run the containers:**

    ```sh
    docker-compose up --build
    ```

2. **Run database migrations:**

    The `command` specified in the `docker-compose.yml` file will automatically run the migrations and start the Django server.

3. **Access the application:**

    Open your browser and go to `http://localhost:8000`.

## Technologies

- Django
- Celery
- Redis
- Docker
