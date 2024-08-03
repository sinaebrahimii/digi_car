from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database import Base

class Category(Base):
    __tablename__ = "categories"

    id :Mapped[int]=mapped_column(primary_key=True)
    name : Mapped[str]