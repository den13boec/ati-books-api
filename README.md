# ATI Books API

REST API-сервис для управления книгами. Реализован на FastAPI + PostgreSQL + SQLAlchemy, обёрнут в Docker.

## ⚙️ Как запустить проект

> Требования: установлен [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/)

```bash
git clone https://github.com/den13boec/ati-books-api
cd ati-books-api
```

Перед запуском необходимо создать .env файл в корне проекта для подключения к БД:

```env
POSTGRES_USER=ati_user
POSTGRES_PASSWORD=ati_pass
POSTGRES_DB=ati_books_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

>POSTGRES_HOST=db — это имя сервиса базы данных в docker-compose.yml

Затем:

```bash
docker compose up --build
```

## Эндпойнты

| Метод | URL           | Описание                                                                                         |
|:-----:|---------------|--------------------------------------------------------------------------------------------------|
|  POST | `/books/`     | Создать новую книгу                                                                              |
| GET   | `/books/`     | Получить список всех книг, с возможностью фильтрации по автору (например, ?author=George Orwell) |
| GET   | `/books/{id}` | Получить информацию о книге по ID                                                                |

>Можно протестировать эндпойнты через [SwaggerUI](http://127.0.0.1:8000/docs) или [Redoc](http://127.0.0.1:8000/redoc)
