from pydantic import BaseModel,ConfigDict

class ProductRequest(BaseModel):
    name:str
    description:str="unique product"
    price:int
    stock_quantity:int=0
    category_id:int|None=None

class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    name:str
    description:str
    price:int
    stock_quantity:int
    category_id:int|None=None

class CategoryRequest(BaseModel):
    name:str