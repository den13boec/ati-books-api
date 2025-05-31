from typing import Annotated
from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: Annotated[str, Field(description="Название книги")]
    author: Annotated[str, Field(description="Имя автора")]
    published_year: Annotated[int, Field(description="Год публикации")]


class Book(BookCreate):
    id: Annotated[int, Field(description="Уникальный идентификатор")]

    model_config = {"from_attributes": True}
