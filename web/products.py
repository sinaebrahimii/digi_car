from fastapi import  APIRouter,Depends
from database import SessionLocal
from sqlalchemy.orm import Session 
from typing import Annotated
from schemas.products import ProductRequest
from models.products import Product

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency= Annotated[Session , Depends(get_db)]

router = APIRouter(prefix="/products",tags=["products"])

@router.get("/")
async def get_all_products(db:db_dependency):
    products=db.query(Product).all()
    return products
    



@router.post("/",status_code=200)
async def create_procuct(db:db_dependency,product:ProductRequest):
    dict=product.model_dump()
    product_model=Product(**product.model_dump())
    db.add(product_model)
    db.commit()
    print(dict)
    return (dict)