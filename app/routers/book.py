from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.book import Book, BookCreate
from app.crud.book import create_book, get_books, get_book_by_id

router = APIRouter()


@router.post(
    "/",
    response_model=Book,
    summary="Создать новую книгу",
    description="Добавляет книгу в базу данных. Все поля обязательны.",
    status_code=201,
    responses={
        400: {"description": "Ошибка валидации — отсутствуют обязательные поля"},
        422: {"description": "Некорректные значения в теле запроса"},
    },
)
def create(
    book: BookCreate,
    db: Session = Depends(get_db),
) -> Book:
    return create_book(db, book)


@router.get(
    "/",
    response_model=list[Book],
    summary="Получить список всех книг",
    description="Возвращает список всех книг. Поддерживает фильтрацию по автору (полное совпадение, без учёта регистра).",
    responses={
        422: {"description": "Некорректные параметры запроса"},
    },
)
def read_books(
    author: str | None = Query(
        default=None,
        description="Имя автора книги",
    ),
    db: Session = Depends(get_db),
) -> list[Book]:
    books = get_books(db, author)
    return books  # type: ignore


@router.get(
    "/{book_id}",
    response_model=Book,
    summary="Получить информацию о книге по ID",
    description="Возвращает одну книгу по её ID. При отсутствии — ошибка 404.",
    responses={
        422: {"description": "Некорректный формат ID"},
    },
)
def read_book(
    book_id: Annotated[int, Path(description="ID книги")],
    db: Session = Depends(get_db),
) -> Book:
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Книга с ID {book_id} не найдена")
    return book  # type: ignore
