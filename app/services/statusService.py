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

