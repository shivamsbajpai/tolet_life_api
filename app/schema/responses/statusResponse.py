from pydantic import BaseModel
from typing import List
from uuid import UUID
class StatusResponse(BaseModel):
    status_id: UUID
    status: str
    class Config():
        orm_mode = True