from pydantic import BaseModel, validator
import re


class UserLoginRequest(BaseModel):
    email: str
    password: str

    @validator("email")
    def email_validation(cls, v):
        if not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", v)):
            raise ValueError('invalid email address')
        return v
