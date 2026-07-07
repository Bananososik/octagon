from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud
from app.db.db import get_db
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[schemas.Book])
def get_books(category_id: int = None, db: Session = Depends(get_db)):
    if category_id is not None:
        return crud.get_books_by_category(db, category_id)
    return crud.get_books(db)


@router.get("/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.create_book(db, book)


@router.put("/{book_id}", response_model=schemas.Book)
def update_book(
    book_id: int,
    book: schemas.BookUpdate,
    db: Session = Depends(get_db),
):
    category = crud.get_category_by_id(db, book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    updated_book = crud.update_book(
        db,
        book_id,
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id,
    )
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@router.delete("/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = crud.delete_book(db, book_id)
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book