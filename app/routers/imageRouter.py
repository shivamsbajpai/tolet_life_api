from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing  import List
from app.data import database
from app.schema.requests.imageDetailsCreateRequest import ImageDetailsCreateRequest
from app.services import imageService
from app.services.authenticationService import AuthHandler


get_db = database.get_db
auth_handler = AuthHandler()


router = APIRouter(
    prefix="/image",
    tags=['Image']
)


@router.get('/sign_s3')
def sign_s3(file_name: str,file_type: str,rent_id:str,user_id=Depends(auth_handler.auth_wrapper)):
    return imageService.presigned_url(file_name,file_type,rent_id)
    
    


@router.post('/uploadimage')
def upload_image(request: ImageDetailsCreateRequest, db: Session = Depends(get_db),user_id=Depends(auth_handler.auth_wrapper)):
    return imageService.save_image_details(user_id,request,db)
