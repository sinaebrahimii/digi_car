from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int]=mapped_column(primary_key=True)
    email:Mapped[str]
    password:Mapped[str]
    role:Mapped[str]
    first_name:Mapped[str]
    last_name:Mapped[str]
    phone_number:Mapped[str]