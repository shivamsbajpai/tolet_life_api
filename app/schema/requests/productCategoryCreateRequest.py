from pydantic import BaseModel
from typing import List


class ProductCategoryCreateRequest(BaseModel):
    product_category: str
