from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database import Base
from models.categories import Category

class Product(Base):
    __tablename__ = "products"

    id:Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str] 
    description: Mapped[str] 
    price: Mapped[int] 
    stock_quantity: Mapped[int] 
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'),nullable=True)
    isbn: Mapped[str]