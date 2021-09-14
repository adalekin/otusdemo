from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from products import schemas
from products.dependencies import get_db
from products.use_cases.products import list_products_user_case

router = APIRouter()


@router.get("/products/", tags=["products"], status_code=200, response_model=List[schemas.Product])
async def list_products(db: Session = Depends(get_db)):
    return list_products_user_case(db=db)
