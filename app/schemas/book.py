from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str = Field(..., description="Название книги")
    author: str = Field(..., description="Имя автора")
    published_year: int = Field(..., description="Год публикации")

class Book(BookCreate):
    id: int = Field(..., description="Уникальный идентификатор")

    model_config = {
        "from_attributes": True
    }
