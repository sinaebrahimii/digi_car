from pydantic import BaseModel,EmailStr,Field

class UserRequest(BaseModel):
    email:EmailStr
    password:str
    role:str
    first_name:str|None=Field(default=None)
    last_name:str|None=Field(default=None)
    phone_number:str|None=Field(default=None)