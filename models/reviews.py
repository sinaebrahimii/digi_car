from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database import Base
from models.users import User
from models.products import Product

class Review(Base):
    __tablename__ = 'reviews'
    id:Mapped[int] =mapped_column(primary_key=True)
    product_id:Mapped[int] =mapped_column(foreign_key=Product.id)
    user_id:Mapped[int] =mapped_column(foreign_key=User.id)
    comment:Mapped[str]
    rating:Mapped[float]
    review_date:Mapped[datetime]
    user=Mapped[User]