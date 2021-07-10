import os
from uuid import UUID
from botocore.config import Config
from botocore.exceptions import ClientError
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from typing  import List
from app.data import database
from app.schema.requests.imageDetailsCreateRequest import ImageDetailsCreateRequest
from app.services import imageService
from app.services.authenticationService import AuthHandler
import boto3
import logging

get_db = database.get_db
auth_handler = AuthHandler()


router = APIRouter(
    prefix="/image",
    tags=['Image']
)


@router.get('/sign_s3')
def sign_s3(file_name: str,file_type: str,rent_id:str,user_id=Depends(auth_handler.auth_wrapper)):
    my_config = Config(
    region_name = 'us-east-2',
    )
    fields = None

    conditions = None

    expiration = 3600

    object_name = f"{rent_id}/{file_name}"

    bucket_name = os.environ.get('S3_BUCKET')
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

    s3_client = boto3.client('s3',    aws_access_key_id=access_key,
                                      aws_secret_access_key=secret_key,
                                      config=my_config)
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    return response
    


@router.post('/uploadimage')
def upload_image(request: ImageDetailsCreateRequest, db: Session = Depends(get_db),user_id=Depends(auth_handler.auth_wrapper)):
    return imageService.save_image_details(user_id,request,db)
