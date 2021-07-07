from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.data import database
from app.schema.requests.otpCreateRequest import OtpCreateRequest
from app.schema.requests.userCreateRequest import UserCreateRequest
from app.schema.requests.userLoginRequest import UserLoginRequest
from app.services import identityService

get_db = database.get_db

router = APIRouter(
    prefix="/identity",
    tags=['Identity']
)


@router.post('/sendotp', status_code=status.HTTP_200_OK)
def send_otp(request: OtpCreateRequest, db: Session = Depends(get_db)):
    return identityService.send_otp_request(request, db)


@router.post('/registeruser', status_code=status.HTTP_201_CREATED)
def register_user(request: UserCreateRequest, db: Session = Depends(get_db)):
    return identityService.register_user(request, db)


@router.post('/loginuser', status_code=status.HTTP_200_OK)
def login_user(request: UserLoginRequest, db: Session = Depends(get_db)):
    return identityService.login_user(request,db)

