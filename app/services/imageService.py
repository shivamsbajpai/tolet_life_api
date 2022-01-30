from datetime import datetime
import os
from botocore.config import Config
from botocore.exceptions import ClientError
from sqlalchemy.orm import Session
from app.models.imageDetails import ImageDetails
from app.schema.requests.imageDetailsCreateRequest import ImageDetailsCreateRequest
import boto3
import logging


def presigned_url(file_name: str,file_type: str,rent_id:str):
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

def save_image_details(user_id:str,request: ImageDetailsCreateRequest, db: Session):
    bucket_name = os.environ.get('S3_BUCKET')
    create_url = f"https://{bucket_name}.s3.us-east-2.amazonaws.com/{request.file_address_aws}"
    image_details = ImageDetails(rent_id=request.rent_id,user_id=user_id,image_url=create_url,last_updated=datetime.utcnow())
    db.add(image_details)
    db.commit()
    db.refresh(image_details)
    return
