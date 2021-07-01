from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.schema.requests.userCreateRequest import UserCreateRequest



def get_all_user_details(db: Session):
    userDetails = db.query(User).all()
    return userDetails


def create_user_details(request: UserCreateRequest, db: Session):
    userDetail = User(**request.dict())
    db.add(userDetail)
    db.commit()
    db.refresh(userDetail)
    return userDetail


def delete_user_details(id: UUID, db: Session):
    userDetail = db.query(User).filter(User.user_id == id)
    if not userDetail.first():
        raise_exception(id)
    userDetail.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def update_user_details(id: UUID, request: UserCreateRequest, db: Session):
    userDetail = db.query(User).filter(User.user_id == id)
    if not userDetail.first():
        raise_exception(id)
    userDetail.update(request.dict())
    db.commit()
    return 'updated'


def get_user_details_by_id(id: UUID, db):
    userDetail = db.query(User).filter(User.user_id == id).first()
    if not userDetail:
        raise_exception(id)
    return userDetail


def raise_exception(id: UUID):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"user details with the id {id} is not available.")
