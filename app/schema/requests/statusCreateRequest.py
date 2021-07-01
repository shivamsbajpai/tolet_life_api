from pydantic import BaseModel
from typing import List

class StatusCreateRequest(BaseModel):
    status: str