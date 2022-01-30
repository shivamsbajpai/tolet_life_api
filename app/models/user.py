import uuid
import sqlalchemy
from ..data.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = 'User'
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    hashed_password = Column(String)
