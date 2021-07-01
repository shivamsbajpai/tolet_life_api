from pydantic import BaseModel
from typing import List
from uuid import UUID
class UserResponse(BaseModel):
    user_id: UUID
    name: str
    phone_number: str
    email: str
    class Config():
        orm_mode = True