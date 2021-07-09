from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.imageDetails import ImageDetails
from app.schema.requests.imageDetailsCreateRequest import ImageDetailsCreateRequest




def save_image_details(user_id:str,request: ImageDetailsCreateRequest, db: Session):
    image_details = ImageDetails(rent_id=request.rent_id,user_id=user_id,image_url=request.image_url)
    db.add(image_details)
    db.commit()
    db.refresh(image_details)
    return



def raise_exception(id: UUID):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"status details with the id {id} is not available.")