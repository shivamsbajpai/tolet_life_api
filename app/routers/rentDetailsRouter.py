from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.data import database
from app.schema.requests.rentDetailsCreateRequest import RentDetailsCreateRequest
from app.services import rentDetailsService
from app.services.authenticationService import AuthHandler

get_db = database.get_db

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/rentdetails",
    tags=['Rent_Details']
)


@router.get('/getallrentdetails')
def get_all_rent_details(db: Session = Depends(database.get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return rentDetailsService.get_all_rent_details(db)

@router.get('/search')
def get_all_rent_details_by_search_term(search_term: str,db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return rentDetailsService.get_all_rent_details_by_search_term(search_term,db)

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_rent_details_by_id(id: UUID, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
    return rentDetailsService.get_rent_details_by_id(id, db)
