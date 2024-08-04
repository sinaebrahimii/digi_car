from fastapi import  APIRouter,Depends,HTTPException
from starlette import status
from database import SessionLocal
from sqlalchemy.orm import Session 
from typing import Annotated
from schemas.users import UserCreateRequest
from models.users import User
from .auth import get_current_user

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency= Annotated[Session , Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user)]

router = APIRouter(prefix="/users",tags=["users"])
@router.get("/",status_code=status.HTTP_200_OK)
async def get_all_users(user:user_dependency,db:db_dependency):
    print(user)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not authenticate user kioni")
    return db.query(User).filter(user.get('id')==User.id).first()