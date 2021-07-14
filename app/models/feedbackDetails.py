import uuid
import sqlalchemy
from ..data.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

class FeedbackDetails(Base):
    __tablename__ = 'FeedbackDetails'
    feeback_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    email = Column(String)
    feedback = Column(String)