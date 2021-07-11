import uuid
import sqlalchemy
from sqlalchemy.sql.sqltypes import DateTime
from ..data.database import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from uuid import UUID
from .user import User
from .status import Status
from sqlalchemy.dialects.postgresql import UUID



class RentDetails(Base):
    __tablename__ = 'RentDetails'
    rent_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey(User.user_id))
    pincode = Column(String)
    address = Column(String)
    area = Column(String)
    city = Column(String)
    state = Column(String)
    monthly_rent = Column(Float)
    last_updated = Column(DateTime)
    status_id = Column(UUID(as_uuid=True), ForeignKey(Status.status_id))
