from app.schema.requests.userProfileUpdateRequest import UserProfileUpdateRequest
from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.data import database
from app.services import userProfileDetailsService
from app.services.authenticationService import AuthHandler
from app.schema.responses.userProfileResponse import UserProfileResponse

get_db = database.get_db

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/userprofiledetails",
    tags=['User_Profile_Details']
)


@router.get('/get',response_model=UserProfileResponse,status_code=status.HTTP_200_OK)
def get_user_profile_details(db: Session = Depends(database.get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return userProfileDetailsService.get_profile_details(user_id,db)


@router.put('/update', status_code=status.HTTP_200_OK)
def update_user_profile_details(request: UserProfileUpdateRequest, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return userProfileDetailsService.update_profile_details(request,user_id, db)

@router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_user_profile_details(delete_string: str, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return userProfileDetailsService.delete_user_profile_details(delete_string,user_id, db)
