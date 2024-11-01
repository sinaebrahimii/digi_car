from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from database import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from schemas.users import UserCreateRequest, UserResponse, UserAddress
from models.users import User
from models.addresses import Address
from .auth import get_current_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user(user: user_dependency, db: db_dependency):
    print(user)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not authenticate user kioni")
    return db.query(User).filter(user.get('id') == User.id).first()


@router.post("/address", status_code=status.HTTP_201_CREATED)
async def create_address(user: user_dependency, db: db_dependency, user_address: UserAddress):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not authenticate user kioni")
    user_address_model = Address(**user_address.model_dump(), user_id=user.get("id"))
    db.add(user_address_model)
    db.commit()
    return user_address.model_dump()
