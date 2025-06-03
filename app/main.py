from fastapi import FastAPI
from app.routers import book
from app.database import Base, engine


app = FastAPI(
    title="ATI Books API",
    version="1.0.0",
    description="REST API для управления книгами",
)

# Placeholder for alembic
Base.metadata.create_all(bind=engine)

app.include_router(book.router, prefix="/books", tags=["Books"])
