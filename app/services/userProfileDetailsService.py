from app.services.userRentDetailsService import delete_rent_details
from app.models.rentDetails import RentDetails
from app.schema.requests.userProfileUpdateRequest import UserProfileUpdateRequest
from uuid import UUID
from sqlalchemy import or_
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.imageDetails import ImageDetails
from app.models.rentDetails import RentDetails


def get_profile_details(user_id: str,db: Session):
    userProfile = db.query(User).filter(User.user_id == user_id).first()
    return userProfile

def update_profile_details(request: UserProfileUpdateRequest,user_id: str,db: Session):
    userProfile = db.query(User).filter(User.user_id == user_id).first()
    if not userProfile:
        raise_exception(user_id)
    if(request.name != ""):
        userProfile.name = request.name
    if(request.phone_number != "+91"):
        userProfile.phone_number = request.phone_number
    db.commit()
    return 'updated'

def delete_user_profile_details(delete_string: str,user_id: str,db: Session):
    if(delete_string.lower() != "delete"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Please type delete to confirm")
    userProfile = db.query(User).filter(User.user_id == user_id)
    if not userProfile.first():
        raise_exception(user_id)
    delete_rent_details(user_id,db)
    userProfile.delete(synchronize_session=False)
    db.commit()
    return 'deleted'

def raise_exception(id: UUID):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"user does not exist")

def delete_image_details(rent_id:str,db: Session):
    image_details_list = db.query(ImageDetails).filter(ImageDetails.rent_id == rent_id)
    if image_details_list.first():
        image_details_list.delete(synchronize_session=False)
        db.commit()
    return


def delete_rent_details(user_id: str,db: Session):
    rentDetail = db.query(RentDetails).filter(RentDetails.user_id == user_id)
    if rentDetail.first():
        for rent in rentDetail:
            delete_image_details(rent.rent_id,db)
        rentDetail.delete(synchronize_session=False)
        db.commit()
    return

