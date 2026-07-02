from app.db.models import Category, Book


def create_category(db, title: str):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db):
    return db.query(Category).all()


def get_category_by_id(db, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def update_category(db, category_id: int, new_title: str):
    category = get_category_by_id(db, category_id)

    if category is None:
        return None

    category.title = new_title
    db.commit()
    db.refresh(category)
    return category


def delete_category(db, category_id: int):
    category = get_category_by_id(db, category_id)

    if category is None:
        return None

    db.delete(category)
    db.commit()
    return category


def create_book(
    db,
    title: str,
    description: str,
    price: float,
    url: str,
    category_id: int
):
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db):
    return db.query(Book).all()


def get_book_by_id(db, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(
    db,
    book_id: int,
    title: str,
    description: str,
    price: float,
    url: str,
    category_id: int
):
    book = get_book_by_id(db, book_id)

    if book is None:
        return None

    book.title = title
    book.description = description
    book.price = price
    book.url = url
    book.category_id = category_id

    db.commit()
    db.refresh(book)
    return book


def delete_book(db, book_id: int):
    book = get_book_by_id(db, book_id)

    if book is None:
        return None

    db.delete(book)
    db.commit()
    return book