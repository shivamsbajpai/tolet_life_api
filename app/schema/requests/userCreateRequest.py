import uuid
from pydantic import BaseModel
from typing import List

class UserCreateRequest(BaseModel):
    name: str
    phone_number: str
    email: str