from datetime import datetime
from typing import List
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.rentDetails import RentDetails
from app.models.imageDetails import ImageDetails
from app.schema.requests.rentDetailsCreateRequest import RentDetailsCreateRequest
from app.schema.responses.rentDetailsResponse import RentDetailsResponse


def get_all_rent_details(user_id:str,db: Session):
    rentDetails = db.query(RentDetails).filter(RentDetails.user_id == user_id).all()
    response = create_response_list(rentDetails,db)
    return response


def create_rent_details(user_id:str,request: RentDetailsCreateRequest, db: Session):
    rentDetails = RentDetails(**request.dict(),user_id=user_id,last_updated = datetime.utcnow())
    db.add(rentDetails)
    db.commit()
    db.refresh(rentDetails)
    return rentDetails


def delete_rent_details(user_id:str,id: UUID, db: Session):
    rentDetail = db.query(RentDetails).filter(RentDetails.rent_id == id).filter(RentDetails.user_id == user_id)
    if not rentDetail.first():
        raise_exception(id)
    rentDetail.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def update_rent_details(user_id: str,id: UUID, request: RentDetailsCreateRequest, db: Session):
    rentDetail = db.query(RentDetails).filter(RentDetails.rent_id == id).filter(RentDetails.user_id == user_id)
    if not rentDetail.first():
        raise_exception(id)
    rentDetail.update(request.dict())
    db.commit()
    return 'updated'


def get_rent_details_by_id(user_id: str,id: UUID, db):
    rentDetail = db.query(RentDetails).filter(
        RentDetails.rent_id == id).filter(RentDetails.user_id == user_id).first()
    if not rentDetail:
        raise_exception(id)
    return rentDetail


def raise_exception(id: UUID):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"rent details with the id {id} is not available.")



def create_response_list(rentDetails,db:Session):
    response_list = list()
    for rent in rentDetails:
        
        response_list.append(create_response(rent,db))
    return response_list


def create_response(rent: RentDetails,db:Session):
    response = RentDetailsResponse()
    image_url_list = get_image_urls(rent.rent_id,db)
    response.rent_id = rent.rent_id
    response.user_id = rent.user_id
    response.address = rent.address
    response.area = rent.area
    response.city = rent.city
    response.state = rent.state
    response.status_id = rent.status_id
    response.monthly_rent = rent.monthly_rent
    response.pincode = rent.pincode
    response.image_urls = image_url_list
    return response


def get_image_urls(rent_id,db:Session):
    image_urls = db.query(ImageDetails).filter(ImageDetails.rent_id == rent_id).all()
    return image_urls
