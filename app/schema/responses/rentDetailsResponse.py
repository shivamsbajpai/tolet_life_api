from pydantic import BaseModel
from typing import List
from uuid import UUID

class RentDetailsResponse():
    rent_id: UUID
    user_id: UUID
    product_name: str
    product_category_id: UUID
    product_description: str
    security_deposit: str
    monthly_rent: str
    owner_name: str
    owner_email: str
    pincode: str
    area: str
    city: str
    state: str
    address: str
    status_id: UUID
    image_urls: list()