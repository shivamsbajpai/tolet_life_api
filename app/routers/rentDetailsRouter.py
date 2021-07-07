from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.data import database
from app.schema.requests.rentDetailsCreateRequest import RentDetailsCreateRequest
from app.schema.responses.rentDetailsResponse import RentDetailsResponse
from app.services import rentDetailsService
from app.services.authenticationService import AuthHandler

get_db = database.get_db

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/rentdetails",
    tags=['Rent_Details']
)


@router.get('/', response_model=List[RentDetailsResponse])
def get_all_rent_details(db: Session = Depends(database.get_db), user=Depends(auth_handler.auth_wrapper)):
    return rentDetailsService.get_all_rent_details(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_rent_details(request: RentDetailsCreateRequest, db: Session = Depends(get_db), user=Depends(auth_handler.auth_wrapper)):
    return rentDetailsService.create_rent_details(request, db)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_rent_details(id: UUID, db: Session = Depends(get_db), user=Depends(auth_handler.auth_wrapper)):
    return rentDetailsService.delete_rent_details(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_rent_details(id: UUID, request: RentDetailsCreateRequest, db: Session = Depends(get_db), user=Depends(auth_handler.auth_wrapper)):
    return rentDetailsService.update_rent_details(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=RentDetailsResponse)
def get_rent_details_by_id(id: UUID, db: Session = Depends(get_db), user=Depends(auth_handler.auth_wrapper)):
    return rentDetailsService.get_rent_details_by_id(id, db)
