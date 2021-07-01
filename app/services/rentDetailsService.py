from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.rentDetails import RentDetails
from app.schema.requests.rentDetailsCreateRequest import RentDetailsCreateRequest



def get_all_rent_details(db: Session):
    rentDetails = db.query(RentDetails).all()
    return rentDetails


def create_rent_details(request: RentDetailsCreateRequest, db: Session):
    rentDetails = RentDetails(**request.dict())
    db.add(rentDetails)
    db.commit()
    db.refresh(rentDetails)
    return rentDetails


def delete_rent_details(id: UUID, db: Session):
    rentDetail = db.query(RentDetails).filter(RentDetails.rent_id == id)
    if not rentDetail.first():
        raise_exception(id)
    rentDetail.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def update_rent_details(id: UUID, request: RentDetailsCreateRequest, db: Session):
    rentDetail = db.query(RentDetails).filter(RentDetails.rent_id == id)
    if not rentDetail.first():
        raise_exception(id)
    rentDetail.update(request.dict())
    db.commit()
    return 'updated'


def get_rent_details_by_id(id: UUID, db):
    rentDetail = db.query(RentDetails).filter(
        RentDetails.rent_id == id).first()
    if not rentDetail:
        raise_exception(id)
    return rentDetail


def raise_exception(id: UUID):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"rent details with the id {id} is not available.")
