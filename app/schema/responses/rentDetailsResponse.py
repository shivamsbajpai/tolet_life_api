from pydantic import BaseModel
from typing import List
from uuid import UUID
class RentDetailsResponse(BaseModel):
    rent_id: UUID
    user_id: UUID
    pincode: str
    address: str
    monthly_rent: float
    status_id: UUID
    class Config():
        orm_mode = True