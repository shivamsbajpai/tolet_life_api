from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.status import Status
from app.schema.requests.statusCreateRequest import StatusCreateRequest


def get_all_status_details(db: Session):
    statusDetails = db.query(Status).all()
    return statusDetails


def create_status_details(request: StatusCreateRequest, db: Session):
    statusDetail = Status(**request.dict())
    db.add(statusDetail)
    db.commit()
    db.refresh(statusDetail)
    return statusDetail


def delete_status_details(id: UUID, db: Session):
    statusDetail = db.query(Status).filter(Status.status_id == id)
    if not statusDetail.first():
        raise_exception(id)
    statusDetail.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def update_status_details(id: UUID, request: StatusCreateRequest, db: Session):
    statusDetail = db.query(Status).filter(Status.status_id == id)
    if not statusDetail.first():
        raise_exception(id)
    statusDetail.update(request.dict())
    db.commit()
    return 'updated'


def get_status_details_by_id(id: UUID, db):
    statusDetail = db.query(Status).filter(
        Status.status_id == id).first()
    if not statusDetail:
        raise_exception(id)
    return statusDetail


def raise_exception(id: UUID):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"status details with the id {id} is not available.")
