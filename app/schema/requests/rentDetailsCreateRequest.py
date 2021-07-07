from uuid import UUID
from pydantic import BaseModel
from typing import List


class RentDetailsCreateRequest(BaseModel):
    pincode: str
    address: str
    monthly_rent: float
    status_id: UUID
