from uuid import UUID
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from typing  import List
from app.data import database
from app.schema.requests.statusCreateRequest import StatusCreateRequest
from app.schema.responses.statusResponse import StatusResponse
from app.services import statusService

get_db = database.get_db

router = APIRouter(
    prefix="/status",
    tags=['Status']
)


@router.get('/', response_model=List[StatusResponse])
def get_all_status_details(db: Session = Depends(database.get_db)):
    return statusService.get_all_status_details(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_status_details(request: StatusCreateRequest, db: Session = Depends(get_db)):
    return statusService.create_status_details(request, db)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_status_details(id: UUID, db: Session = Depends(get_db)):
    return statusService.delete_status_details(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_status_details(id: UUID, request: StatusCreateRequest, db: Session = Depends(get_db)):
    return statusService.update_status_details(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=StatusResponse)
def get_status_details_by_id(id: UUID, db: Session = Depends(get_db)):
    return statusService.get_status_details_by_id(id, db)
