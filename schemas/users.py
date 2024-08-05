from pydantic import BaseModel,EmailStr,Field

class UserCreateRequest(BaseModel):
    email:EmailStr
    password:str=Field(min_length=8)
    role:str|None=None
    first_name:str|None=None
    last_name:str|None=None
    phone_number:str|None=None

class Token(BaseModel):
    access_token:str
    token_type:str