import uuid
import sqlalchemy
from ..data.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

class OtpHistory(Base):
    __tablename__ = 'OtpHistory'
    otp_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String)
    otp_code = Column(String)