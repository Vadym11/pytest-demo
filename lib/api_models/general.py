from typing import List, TypeVar, Generic
from pydantic import BaseModel

# T is a placeholder for any model (Product, Brand, etc.)
T = TypeVar("T")

class PaginatedResponse(BaseModel, Generic[T]):
    current_page: int
    data: List[T]
    from_item: int  # 'from' is a reserved keyword in Python, so we rename it
    last_page: int
    per_page: int
    to: int
    total: int

    # This mapping handles the API's "from" key to our "from_item" field
    class Config:
        fields = {'from_item': 'from'}

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

class SuccessResponse(BaseModel):
    success: bool

class LogOutResponse(BaseModel):
    message: str
