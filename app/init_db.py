from app import schemas
from app.db.db import Base, engine, SessionLocal
from app.db import crud
from app.db import models


def init_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        programming = crud.create_category(
            db,
            schemas.CategoryCreate(title="Programming"),
        )
        fiction = crud.create_category(
            db,
            schemas.CategoryCreate(title="Fiction"),
        )

        crud.create_book(
            db,
            schemas.BookCreate(
                title="Python",
                description="Learn Python",
                price=1200,
                url="",
                category_id=programming.id,
            ),
        )
        crud.create_book(
            db,
            schemas.BookCreate(
                title="SQL",
                description="Databases",
                price=1500,
                url="",
                category_id=programming.id,
            ),
        )
        crud.create_book(
            db,
            schemas.BookCreate(
                title="Book 1",
                description="Story",
                price=900,
                url="",
                category_id=fiction.id,
            ),
        )
        crud.create_book(
            db,
            schemas.BookCreate(
                title="Book 2",
                description="Story",
                price=800,
                url="",
                category_id=fiction.id,
            ),
        )

        print("OK DB CREATED")

    finally:
        db.close()


if __name__ == "__main__":
    init_database()