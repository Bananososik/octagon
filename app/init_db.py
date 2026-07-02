from app.db.db import Base, engine, SessionLocal
from app.db import crud
from app.db import models


def init_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        programming = crud.create_category(db, "Программирование")
        fiction = crud.create_category(db, "Художественная литература")

        crud.create_book(db, "Python", "Learn Python", 1200, "", programming.id)
        crud.create_book(db, "SQL", "Databases", 1500, "", programming.id)
        crud.create_book(db, "Book 1", "Story", 900, "", fiction.id)
        crud.create_book(db, "Book 2", "Story", 800, "", fiction.id)

        print("OK DB CREATED")

    finally:
        db.close()


if __name__ == "__main__":
    init_database()