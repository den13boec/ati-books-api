from typing import Annotated
from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class BookCreate(BaseModel):
    title: Annotated[str, Field(description="Название книги")]
    author: Annotated[str, Field(description="Имя автора книги")]
    published_year: Annotated[int, Field(description="Год публикации книги")]

    @field_validator("title", "author", mode="before")
    @classmethod
    def not_empty(cls, value: str, info) -> str:
        if not value or not value.strip():
            raise ValueError(f"Поле '{info.field_name}' не может быть пустым")
        return value

    @field_validator("published_year")
    @classmethod
    def not_in_future(cls, value: int) -> int:
        current_year = datetime.now().year
        if value > current_year:
            raise ValueError(f"Год публикации не может быть больше {current_year}")
        return value


class Book(BookCreate):
    id: Annotated[int, Field(description="Уникальный идентификатор книги")]

    model_config = {"from_attributes": True}
