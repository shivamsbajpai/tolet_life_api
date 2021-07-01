import uuid
import sqlalchemy
from ..data.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class Status(Base):
    __tablename__ = 'Status'
    status_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(String)

