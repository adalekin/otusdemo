from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from payments import schemas
from payments.dependencies import get_db
from payments.use_cases.payments import confirm_payment_use_case, create_payment_use_case

router = APIRouter()


@router.post("/payments/", tags=["payments"], status_code=201, response_model=schemas.Payment)
async def create_payment(create_payment: schemas.CreatePayment, db: Session = Depends(get_db)):
    return create_payment_use_case(create_payment=create_payment, db=db)


@router.post("/payments/{payment_id}/confirm/", tags=["payments"], status_code=200)
async def confirm_payment(payment_id: int, db: Session = Depends(get_db)):
    return await confirm_payment_use_case(payment_id=payment_id, db=db)
