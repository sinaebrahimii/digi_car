from fastapi import  APIRouter,Depends
from database import SessionLocal
from sqlalchemy.orm import Session 
from typing import Annotated
from schemas.users import UserRequest
from models.users import User

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency= Annotated[Session , Depends(get_db)]

router = APIRouter(prefix="/users",tags=["users"])

@router.post('/')
async def create_user(db:db_dependency,user:UserRequest):
    user_model=User(**user.model_dump())
    db.add(user_model)
    db.commit()
    return("user created")