from pydantic import BaseModel
from typing import List
from uuid import UUID
from app.common.imageResponse import ImageResponse

class UserProfileResponse(BaseModel):
    user_id: UUID
    name: str
    email: str
    phone_number: str
    class Config():
        orm_mode = True