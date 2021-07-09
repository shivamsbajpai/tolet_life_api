from uuid import UUID
from pydantic import BaseModel
from typing import List


class ImageDetailsCreateRequest(BaseModel):
    rent_id: UUID
    image_url: str
