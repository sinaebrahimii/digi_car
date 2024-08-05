from  pydantic import BaseModel,ConfigDict
from datetime import datetime
class ReviewCreate(BaseModel):
    user_id:int
    product_id:int
    rating:float
    comment:str
    review_date:datetime=datetime.now()