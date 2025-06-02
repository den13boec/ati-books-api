from sqlalchemy import Column, Integer, String
from app.database import Base


class Book(Base):
    __tablename__ = "books"
    __table_args__ = {"comment": "Таблица книг"}

    id = Column(
        Integer, primary_key=True, index=True, comment="Уникальный идентификатор книги"
    )
    title = Column(String, nullable=False, comment="Название книги")
    author = Column(String, nullable=False, comment="Имя автора книги")
    published_year = Column(Integer, nullable=False, comment="Год публикации книги")
