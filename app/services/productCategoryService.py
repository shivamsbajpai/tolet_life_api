from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.productCategory import ProductCategory
from app.schema.requests.productCategoryCreateRequest import ProductCategoryCreateRequest


def get_all_product_categories(db: Session):
    product_categories = db.query(ProductCategory).all()
    return product_categories


def create_product_category(request: ProductCategoryCreateRequest, db: Session):
    product_category = ProductCategory(**request.dict())
    db.add(product_category)
    db.commit()
    db.refresh(product_category)
    return product_category

