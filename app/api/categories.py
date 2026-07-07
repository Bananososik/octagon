from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud
from app.db.db import get_db
from app import schemas

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[schemas.Category])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/", response_model=schemas.Category, status_code=201)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@router.put("/{category_id}", response_model=schemas.Category)
def update_category(
    category_id: int,
    category: schemas.CategoryUpdate,
    db: Session = Depends(get_db),
):
    updated_category = crud.update_category(db, category_id, category.title)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category


@router.delete("/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    deleted_category = crud.delete_category(db, category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category