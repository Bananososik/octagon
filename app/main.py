from app.db.db import SessionLocal
from app.db import crud


def main():
    db = SessionLocal()

    try:
        categories = crud.get_categories(db)

        print("Категории и книги:")
        print("-" * 40)

        for category in categories:
            print(f"Категория: {category.title}")

            for book in category.books:
                print(f"  Книга: {book.title}")
                print(f"  Описание: {book.description}")
                print(f"  Цена: {book.price}")
                print(f"  URL: {book.url}")
                print()

            print("-" * 40)

    finally:
        db.close()


if __name__ == "__main__":
    main()