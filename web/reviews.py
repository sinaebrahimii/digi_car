from fastapi import APIRouter, Depends, HTTPException, Path
from database import SessionLocal
from starlette import status
from sqlalchemy.orm import Session
from typing import Annotated
from schemas.reviews import ReviewCreate
from models.reviews import Review
from .auth import get_current_user
from datetime import datetime


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.get("/{product_id}", status_code=status.HTTP_200_OK)
async def get_product_reviews(db: db_dependency, product_id: int = Path(gt=0)):
    reviews = db.query(Review).filter(Review.product_id == product_id).all()
    return reviews


@router.post("/{product_id}", status_code=status.HTTP_201_CREATED)
async def create_product_review(user: user_dependency, db: db_dependency,review: ReviewCreate,product_id: int = Path(gt=0)):
    review.review_date = datetime.now()
    review_model = Review(**review.model_dump())
    db.add(review_model)
    db.commit()
    return review.model_dump()