from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import List, Literal


class UserCreateRequest(BaseModel):
    email: EmailStr
    password: str
    role: Literal["user", "admin"] = "user"
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class UserReviewResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: str
    last_name: str


class UserAddress(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = Field(default=None, gt=0)
    postal_code: str
    city: str
    street: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    role: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    addresses: List[UserAddress] | None = None
