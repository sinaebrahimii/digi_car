from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped,relationship,mapped_column
from database import Base
from models.categories import Category
from typing import List
class Product(Base):
    __tablename__ = "products"

    id:Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str] 
    description: Mapped[str] 
    price: Mapped[int] 
    stock_quantity: Mapped[int] 
    category_id: Mapped[int] = mapped_column(ForeignKey(Category.id),nullable=True)
    images: Mapped[List["Image"]] = relationship(back_populates="product")