from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.data import database
from app.schema.requests.rentDetailsCreateRequest import RentDetailsCreateRequest
from app.services import userRentDetailsService
from app.services.authenticationService import AuthHandler

get_db = database.get_db

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/user/rentdetails",
    tags=['User_Rent_Details']
)


@router.get('/')
def user_get_all_rent_details(db: Session = Depends(database.get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return userRentDetailsService.get_all_rent_details(user_id,db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def user_create_rent_details(request: RentDetailsCreateRequest, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return userRentDetailsService.create_rent_details(user_id,request, db)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def user_delete_rent_details(id: UUID, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return userRentDetailsService.delete_rent_details(user_id,id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def user_update_rent_details(id: UUID, request: RentDetailsCreateRequest, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return userRentDetailsService.update_rent_details(user_id,id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK)
def user_get_rent_details_by_id(id: UUID, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return userRentDetailsService.get_rent_details_by_id(user_id,id, db)
