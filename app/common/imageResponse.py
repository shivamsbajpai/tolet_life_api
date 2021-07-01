from pydantic import BaseModel
from typing import List
from uuid import UUID

class ImageResponse(BaseModel):
    image_id: UUID
    image_url: str