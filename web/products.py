from fastapi import  APIRouter,Depends,Path,HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session 
from typing import Annotated
from schemas.products import ProductRequest,ProductResponse
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

@router.get("/{product_id}",response_model=ProductResponse)
async def get_product(db: db_dependency,product_id: int=Path(gt=0)):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product



@router.post("/",status_code=200)
async def create_procuct(db:db_dependency,product:ProductRequest):
    dict=product.model_dump()
    product_model=Product(**dict)
    db.add(product_model)
    db.commit()
    print(dict)
    return (product.model_dump())

@router.put("/{product_id}")
async def update_product(db:db_dependency,product_id: int, product_request: ProductRequest, ):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.name = product_request.name
    product.description = product_request.description
    product.price = product_request.price
    product.stock_quantity = product_request.stock_quantity
    
    if product_request.category_id is not None:
        product.category_id = product_request.category_id
    
    db.commit()
    
    db.refresh(product)
    
    return product

@router.delete("/{product_id}")
async def delete_product( db: db_dependency,product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted successfully"}