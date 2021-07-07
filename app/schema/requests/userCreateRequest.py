import re
from pydantic import BaseModel, validator
from typing import List


class UserCreateRequest(BaseModel):
    name: str
    phone_number: str
    email: str
    otp_code: str
    password: str

    @validator("email")
    def email_validation(cls, v):
        if not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", v)):
            raise ValueError('invalid email address')
        return v

    @validator("phone_number")
    def phone_validation(cls, v):
        if not bool(re.search("^\\+[1-9]\\d{1,14}$", v)):
            raise ValueError('invalid phone number')
        if not len(v) == 13:
            raise ValueError('length of phone number should be 10')
        return v
