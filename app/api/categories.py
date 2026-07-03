from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud
from app.db.db import get_db
from app import schemas

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Not found")
    return category


@router.post("/", status_code=201)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return crud.delete_category(db, category_id)