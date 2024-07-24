from fastapi import  APIRouter,Depends,HTTPException
from database import SessionLocal
from starlette import status
from sqlalchemy.orm import Session 
from typing import Annotated
from schemas.products import ProductRequest
from models.categories import Category


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency= Annotated[Session , Depends(get_db)]

router=APIRouter(prefix="/categories",tags=["categories"])


@router.get("/",status_code=status.HTTP_200_OK)
async def get_all_categories(db:db_dependency):
    categories=db.query(Category).all()
    return categories

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_category(db:db_dependency,category:str):
    category_model=Category(name=category)
    db.add(category_model)
    db.commit()
    return ("Item created successfully")

