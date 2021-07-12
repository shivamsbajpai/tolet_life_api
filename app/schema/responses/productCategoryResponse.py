from pydantic import BaseModel
from typing import List
from uuid import UUID

class ProductCategoryResponse(BaseModel):
    product_category_id: UUID
    product_category: str
    class Config():
        orm_mode = True