from app.models.user import User
from uuid import UUID
from sqlalchemy import or_
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.rentDetails import RentDetails
from app.schema.requests.rentDetailsCreateRequest import RentDetailsCreateRequest
from app.services import userRentDetailsService


def get_all_rent_details(db: Session):
    rentDetails = db.query(RentDetails).all()
    response = userRentDetailsService.create_response_list(rentDetails, db)
    return response


def get_all_rent_details_by_address_search_term(search_term: str, db: Session):
    rentDetails = db.query(RentDetails).filter(or_(RentDetails.address.ilike(f"%{search_term}%"), RentDetails.area.ilike(
        f"%{search_term}%"), RentDetails.city.ilike(f"{search_term}%"), RentDetails.state.ilike(f"%{search_term}%"))).all()
    response = userRentDetailsService.create_response_list(rentDetails, db)
    return response


def get_all_rent_details_by_product_search_term(search_term: str, db: Session):
    rentDetails = db.query(RentDetails).filter(or_(RentDetails.product_name.ilike(f"%{search_term}%"), RentDetails.product_description.ilike(
        f"%{search_term}%"))).all()
    response = userRentDetailsService.create_response_list(rentDetails, db)
    return response


def get_rent_details_by_id(id: UUID, db):
    rentDetail = db.query(RentDetails).filter(
        RentDetails.rent_id == id).first()
    if not rentDetail:
        raise_exception(id)
    return rentDetail



def raise_exception(id: UUID):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"rent details with the id {id} is not available.")
