from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from typing  import List
from app.data import database
from app.schema.requests.productCategoryCreateRequest import ProductCategoryCreateRequest
from app.schema.responses.productCategoryResponse import ProductCategoryResponse
from app.services import productCategoryService
from app.services.authenticationService import AuthHandler


get_db = database.get_db
auth_handler = AuthHandler()


router = APIRouter(
    prefix="/productcategory",
    tags=['Product_Category']
)


@router.get('/', response_model=List[ProductCategoryResponse])
def get_all_product_categories(db: Session = Depends(database.get_db), user=Depends(auth_handler.auth_wrapper)):
    return productCategoryService.get_all_product_categories(db)

