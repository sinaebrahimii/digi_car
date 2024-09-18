from  pydantic import BaseModel,ConfigDict
from datetime import datetime
from .users import UserReviewResponse
class ReviewCreate(BaseModel):
    rating:float
    comment:str
    review_date:datetime=datetime.now()

class ReviewResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id:int
    user_id:int
    product_id:int
    rating:float
    comment:str
    review_date:datetime
    user:UserReviewResponse