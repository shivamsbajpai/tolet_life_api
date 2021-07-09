import uuid
import sqlalchemy
from ..data.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from .rentDetails import RentDetails
from .user import User

class ImageDetails(Base):
    __tablename__ = 'ImageDetails'
    image_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rent_id = Column(UUID(as_uuid=True), ForeignKey(RentDetails.rent_id))
    user_id = Column(UUID(as_uuid=True), ForeignKey(User.user_id))
    image_url = Column(String)