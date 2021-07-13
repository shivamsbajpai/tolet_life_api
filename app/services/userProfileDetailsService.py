from app.schema.requests.userProfileUpdateRequest import UserProfileUpdateRequest
from uuid import UUID
from sqlalchemy import or_
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User


def get_profile_details(user_id: str,db: Session):
    userProfile = db.query(User).filter(User.user_id == user_id).first()
    return userProfile

def update_profile_details(request: UserProfileUpdateRequest,user_id: str,db: Session):
    userProfile = db.query(User).filter(User.user_id == user_id).first()
    if not userProfile:
        raise_exception(user_id)
    userProfile.name = request.name
    userProfile.phone_number = request.phone_number
    db.commit()
    return 'updated'

def raise_exception(id: UUID):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"user does not exist")


