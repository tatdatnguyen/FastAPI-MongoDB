from fastapi import FastAPI, HTTPException
from db import database
from typing import List
from models import Book, BookInResponse
from bson import ObjectId

app = FastAPI()

# Hàm trợ giúp chuyển đổi ObjectId thành string
def book_helper(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "publish_year": book["publish_year"],
        "price": book["price"],
    }

# Route để lấy tất cả sách
@app.get("/books/", response_model=List[BookInResponse])
async def get_books():
    books_collection = database.get_collection("books")
    books = await books_collection.find().to_list(1000)
    return [book_helper(book) for book in books]

# Route để thêm sách
@app.post("/books/", response_model=BookInResponse)
async def create_book(book: Book):
    books_collection = database.get_collection("books")
    new_book = await books_collection.insert_one(book.dict())
    created_book = await books_collection.find_one({"_id": new_book.inserted_id})
    return book_helper(created_book)

# Route để lấy sách theo ID
@app.get("/books/{book_id}", response_model=BookInResponse)
async def get_book(book_id: str):
    books_collection = database.get_collection("books")
    book = await books_collection.find_one({"_id": ObjectId(book_id)})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_helper(book)
