from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database import Base
from models.users import User

class Address(Base):
    __tablename__ = 'addresses'
    id:Mapped[int]=mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey(User.id))
    postal_code:Mapped[str]
    city:Mapped[str]
    street:Mapped[str]
