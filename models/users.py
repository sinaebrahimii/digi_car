from datetime import datetime
from sqlalchemy.orm import mapped_column,relationship,Mapped
from database import Base
from models.products import Product
from sqlalchemy import ForeignKey


class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int]=mapped_column(primary_key=True)
    email:Mapped[str]=mapped_column(unique=True)
    password:Mapped[str]
    role:Mapped[str]=mapped_column(default="user")
    first_name:Mapped[str]=mapped_column(nullable=True)
    last_name:Mapped[str]=mapped_column(nullable=True)
    phone_number:Mapped[str]=mapped_column(nullable=True)


