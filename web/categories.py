from fastapi import  APIRouter,Depends,HTTPException,Path
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

@router.put('/{category_id}',status_code=status.HTTP_201_CREATED)
async def update_category(db:db_dependency,category_name:str,category_id:int=Path(gt=0)):
    category=db.query(Category).filter(Category.id==category_id).first()
    if category is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Category not found")
    category.name=category_name
    print(category_name)
    db.add(category)
    db.commit()
    return("Category updated.")

@router.delete('/{category_id}',status_code=status.HTTP_200_OK)
async def delete_category(db:db_dependency,category_id:int =Path(gt=0)):
    category=db.query(Category).filter(Category.id==category_id).first()
    if category is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Category not found")
    db.query(Category).filter(Category.id==category_id).delete()
    db.commit()
    return("Category Deleted.")
