import re
from pydantic import BaseModel, validator
from typing import List


class UserProfileUpdateRequest(BaseModel):
    name: str
    phone_number: str

    @validator("phone_number")
    def phone_validation(cls, v):
        if v == "+91":
            return v
        if not bool(re.search("^\\+[1-9]\\d{1,14}$", v)):
            raise ValueError('invalid phone number')
        if not len(v) == 13:
            raise ValueError('length of phone number should be 10')
        return v
