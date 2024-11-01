from fastapi import APIRouter, Depends, Path, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import Annotated
from schemas.products import ProductRequest, ProductResponse
from models.products import Product, Category
from typing import List


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(db: db_dependency, product_id: int = Path(gt=0)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.get("/category/{category_name}", response_model=List[ProductResponse])
async def get_all_products(
        db: db_dependency,
        category_name: str,
        limit: int = Query(10, ge=5, le=20, description="limit for pagination"),
        page: int = Query(1, ge=1, description="page for pagination")):
    category = db.query(Category).filter(Category.name == category_name).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    offset = (page - 1) * limit
    products = db.query(Product).filter(Product.category_id == category.id).offset(offset).limit(limit).all()
    if products is None:
        raise HTTPException(status_code=404, detail="No products found")
    return products


@router.post("/", status_code=200)
async def create_product(db: db_dependency, product: ProductRequest):
    product_db = product.model_dump()
    product_model = Product(**product_db)
    db.add(product_model)
    db.commit()
    print(product_db)
    return product.model_dump()


@router.put("/{product_id}")
async def update_product(db: db_dependency, product_id: int, product_request: ProductRequest, ):
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
async def delete_product(db: db_dependency, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return {"detail": "Product deleted successfully"}
