from uuid import UUID
from pydantic import BaseModel, validator
from typing import List
import re


class OtpCreateRequest(BaseModel):
    email: str

    @validator("email")
    def email_validation(cls, v):
        if not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", v)):
            raise ValueError('invalid email address')
        return v
