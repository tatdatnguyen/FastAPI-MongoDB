from pydantic import BaseModel
from typing import List, Optional
# La cau truc du lieu de gui request
class Book(BaseModel):
    title: str
    author: str
    publish_year: int
    price: float
# La mo hinh voi truong id them vao khi tra ket qua
class BookInResponse(Book):
    id: str
