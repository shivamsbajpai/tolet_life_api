import uuid
import sqlalchemy
from sqlalchemy.sql.sqltypes import DateTime
from ..data.database import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from uuid import UUID
from .user import User
from .status import Status
from .productCategory import ProductCategory
from sqlalchemy.dialects.postgresql import UUID



class RentDetails(Base):
    __tablename__ = 'RentDetails'
    rent_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey(User.user_id))
    product_name = Column(String)
    product_category_id = Column(UUID(as_uuid=True), ForeignKey(ProductCategory.product_category_id))
    product_description = Column(String)
    security_deposit = Column(String)
    monthly_rent = Column(String)
    pincode = Column(String)
    address = Column(String)
    area = Column(String)
    city = Column(String)
    state = Column(String)
    last_updated = Column(DateTime)
    status_id = Column(UUID(as_uuid=True), ForeignKey(Status.status_id))
