from uuid import UUID
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from typing  import List
from app.data import database
from app.schema.requests.userCreateRequest import UserCreateRequest
from app.schema.responses.userResponse import UserResponse
from app.services import userService

get_db = database.get_db

router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.get('/', response_model=List[UserResponse])
def get_all_user_details(db: Session = Depends(database.get_db)):
    return userService.get_all_user_details(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user_details(request: UserCreateRequest, db: Session = Depends(get_db)):
    return userService.create_user_details(request, db)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_user_details(id: UUID, db: Session = Depends(get_db)):
    return userService.delete_user_details(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_status_details(id: UUID, request: UserCreateRequest, db: Session = Depends(get_db)):
    return userService.update_user_details(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=UserResponse)
def get_user_details_by_id(id: UUID, db: Session = Depends(get_db)):
    return userService.get_user_details_by_id(id, db)
