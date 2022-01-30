from pydantic import BaseModel
from typing import List
from uuid import UUID
from app.common.imageResponse import ImageResponse

class ImageDetailsResponse(BaseModel):
    rent_id: UUID
    image_details: list(ImageResponse)
    class Config():
        orm_mode = True