from uuid import UUID
from pydantic import BaseModel
from typing import List

class RentDetailsCreateRequest(BaseModel):
    user_id: UUID
    pincode: str
    address: str
    monthly_rent: float
    status_id: UUID