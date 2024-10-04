from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from database import Base
from models.products import Product

class Image(Base):
    __tablename__ = "images"

    id:Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str] 
    url: Mapped[str] 
    product_id: Mapped[int] =mapped_column(ForeignKey(Product.id),nullable=True)
    product:Mapped["Product"]=relationship(back_populates="images")
