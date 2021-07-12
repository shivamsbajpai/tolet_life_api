from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from typing  import List
from app.data import database
from app.schema.requests.statusCreateRequest import StatusCreateRequest
from app.schema.responses.statusResponse import StatusResponse
from app.services import statusService
from app.services.authenticationService import AuthHandler


get_db = database.get_db
auth_handler = AuthHandler()


router = APIRouter(
    prefix="/status",
    tags=['Status']
)


@router.get('/', response_model=List[StatusResponse])
def get_all_status_details(db: Session = Depends(database.get_db), user=Depends(auth_handler.auth_wrapper)):
    return statusService.get_all_status_details(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_status_details(request: StatusCreateRequest, db: Session = Depends(get_db), user=Depends(auth_handler.auth_wrapper)):
    return statusService.create_status_details(request, db)
