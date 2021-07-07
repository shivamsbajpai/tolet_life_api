from app.models.otpHistory import OtpHistory
from app.models.user import User
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schema.requests.otpCreateRequest import OtpCreateRequest
from app.schema.requests.userCreateRequest import UserCreateRequest
from app.schema.requests.userLoginRequest import UserLoginRequest
from random import randrange
from . import sendEmailService
from .authenticationService import AuthHandler

auth_handler = AuthHandler()


def send_otp_request(request: OtpCreateRequest, db: Session):
    otp_int = randrange(100000, 999999)
    otp = str(otp_int)
    otp_exists = db.query(OtpHistory).filter(
        OtpHistory.email == request.email).first()
    if otp_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Otp already sent to {request.email}. Please check your spam folder.")
    user_exists = db.query(User).filter(User.email == request.email).first()
    if user_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Email already registered. Please login.")
    subject = sendEmailService.otp_email_subject()
    body = sendEmailService.otp_email_body(otp)
    sendEmailService.send_email(request.email, subject, body)

    save_otp = OtpHistory(email=request.email, otp_code=otp)
    db.add(save_otp)
    db.commit()
    db.refresh(save_otp)
    return


def register_user(request: UserCreateRequest, db: Session):
    email_exists = db.query(User).filter(User.email == request.email).filter(
        User.phone_number == request.phone_number).first()
    if email_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="email/phone_number already exists")

    verify_otp(request.email, request.otp_code, db)

    hashed_pass = auth_handler.get_password_hash(request.password)

    user = User(name=request.name, email=request.email,
                phone_number=request.phone_number, hashed_password=hashed_pass)
    db.add(user)
    db.commit()
    db.refresh(user)

    return


def login_user(request: UserLoginRequest, db: Session):
    email_exists = db.query(User).filter(User.email == request.email).first()
    if (not email_exists) or (not auth_handler.verify_password(request.password, email_exists.hashed_password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    user_id = str(email_exists.user_id)
    token = auth_handler.encode_token(user_id)
    return {'token': token}


def verify_otp(email: str, otp: str, db: Session):
    otp_check = db.query(OtpHistory).filter(
        OtpHistory.otp_code == otp).filter(OtpHistory.email == email)
    if not otp_check.first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect otp")
    otp_check.delete(synchronize_session=False)
    return
