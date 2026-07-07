from pydantic import BaseModel, ConfigDict

class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookBase(BaseModel):
    title: str
    description: str
    price: float
    url: str
    category_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)