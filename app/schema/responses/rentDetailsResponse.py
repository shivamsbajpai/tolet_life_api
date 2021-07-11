from pydantic import BaseModel
from typing import List
from uuid import UUID

class RentDetailsResponse():
    rent_id: UUID
    user_id: UUID
    pincode: str
    area: str
    city: str
    state: str
    address: str
    monthly_rent: float
    status_id: UUID
    image_urls: list()