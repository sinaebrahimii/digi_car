from pydantic import BaseModel

class ProductRequest(BaseModel):
    name:str
    description:str
    price:int
    stock_quantity:int
    category_id:int|None=None
    isbn:str