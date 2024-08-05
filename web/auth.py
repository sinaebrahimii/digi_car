from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.users import Token,UserCreateRequest
from models.users import User
from starlette import status
from passlib.context import CryptContext
from jose import jwt, JWTError

router=APIRouter(prefix='/auth', tags=['auth'])
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "xlntuzhvi3uqri9v3pbehinzk36oljp3"
ALGORITHM = "HS256"
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session , Depends(get_db)]

def authenticate_user(email:str,password:str,db):
    user=db.query(User).filter(User.email==email).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.password):
        return False
    return user

def create_access_token(email:str,user_id:int,role:str, expires_delta: timedelta = timedelta):
    expires = datetime.utcnow() + expires_delta
    encode={"email":email,"id":user_id,"exp":expires}
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id=payload.get("id")
        email=payload.get("email")
        role=payload.get("role")
        if email is None or  id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not authenticate the user")
        return {"email":email,"id":id,"role":role}
    except JWTError :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate user")


@router.post('/',status_code=201)
async def create_user(db:db_dependency,user:UserCreateRequest):
    user_model=User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        role=user.role,
        phone_number=user.phone_number,
        password=bcrypt_context.hash(user.password),)
    db.add(user_model)
    db.commit()
    return("user created")

@router.post("/token",response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
                                 db:db_dependency):
    #uf user and pass is ok returns user or else returns false
    print(form_data.username)
    user= authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate user")
    token = create_access_token(user.email,user.id,user.role,expires_delta=timedelta(minutes=20))
    return  {"access_token":token,"token_type":"bearer"}