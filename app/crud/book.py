from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate


def create_book(db: Session, book: BookCreate) -> Book:
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, author: str | None = None) -> list[Book]:
    query = db.query(Book)
    if author:
        query = query.filter(Book.author.ilike(author))
    return query.all()


def get_book_by_id(db: Session, book_id: int) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()
