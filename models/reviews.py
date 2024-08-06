from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column,relationship,Mapped
from database import Base
from models.users import User
from models.products import Product

class Review(Base):
    __tablename__ = 'reviews'
    id:Mapped[int] =mapped_column(primary_key=True)
    product_id:Mapped[int] =mapped_column(ForeignKey(Product.id))
    user_id:Mapped[int] =mapped_column(ForeignKey(User.id))
    comment:Mapped[str]
    rating:Mapped[float]
    review_date:Mapped[datetime]
    user:Mapped[User]=relationship(User)

