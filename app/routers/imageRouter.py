import os
from uuid import UUID
from botocore.config import Config
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from typing  import List
from app.data import database
from app.schema.requests.imageDetailsCreateRequest import ImageDetailsCreateRequest
from app.services import imageService
from app.services.authenticationService import AuthHandler
import boto3


get_db = database.get_db
auth_handler = AuthHandler()


router = APIRouter(
    prefix="/image",
    tags=['Image']
)


@router.get('/sign_s3')
def sign_s3(file_name: str,file_type: str,db: Session = Depends(database.get_db)):
    #, config = Config(signature_version = 's3v4')
    S3_BUCKET = os.environ.get('S3_BUCKET')
    s3 = boto3.client('s3')

    presigned_post = s3.generate_presigned_post(
        Bucket = S3_BUCKET,
        Key = file_name,
        Fields = {"acl":"public_read","Content-Type": file_type},
        Conditions = [
            {"acl":"public-read"},
            {"Content-Type":file_type}
        ],
        ExpiresIn = 3600
    )
    return {
        'data':presigned_post,
        'url':'https://%s.s3.amazonaws.com/%s'%(S3_BUCKET,file_name)
    }


@router.post('/uploadimage')
def upload_image(request: ImageDetailsCreateRequest, db: Session = Depends(get_db)):
    user_id = "783e3419-e6e7-458a-8b6b-094360231848"
    return imageService.save_image_details(user_id,request,db)
