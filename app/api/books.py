from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud
from app.db.db import get_db
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def get_books(category_id: int = None, db: Session = Depends(get_db)):
    if category_id:
        return crud.get_books_by_category(db, category_id)
    return crud.get_books(db)


@router.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Not found")
    return book


@router.post("/", status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db, book_id)