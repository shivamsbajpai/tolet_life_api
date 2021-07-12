import uuid
import sqlalchemy
from ..data.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class ProductCategory(Base):
    __tablename__ = 'ProductCategory'
    product_category_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_category = Column(String)