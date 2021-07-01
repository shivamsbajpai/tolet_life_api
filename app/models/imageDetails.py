import uuid
import sqlalchemy
from ..data.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from .rentDetails import RentDetails

class ImageDetails(Base):
    __tablename__ = 'ImageDetails'
    image_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rent_id = Column(UUID(as_uuid=True), ForeignKey(RentDetails.rent_id))
    image_url = Column(String)