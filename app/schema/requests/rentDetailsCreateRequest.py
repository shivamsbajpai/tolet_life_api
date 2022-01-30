from uuid import UUID
from pydantic import BaseModel
from typing import List


class RentDetailsCreateRequest(BaseModel):
    product_name: str
    product_category_id: UUID
    product_description: str
    security_deposit: str
    monthly_rent: str
    pincode: str
    address: str
    area: str
    city: str
    state: str
    status_id: UUID
