from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from products import schemas
from products.dependencies import get_db
from products.use_cases.reservations import (
    confirm_reservation_use_case,
    create_reservation_use_case,
)

router = APIRouter()


@router.post("/reservations/", tags=["reservations"], status_code=201, response_model=schemas.Reservation)
async def create_reservation(create_reservation: schemas.CreateReservation, db: Session = Depends(get_db)):
    return create_reservation_use_case(create_reservation=create_reservation, db=db)


@router.post("/reservations/{reservation_id}/confirm/", tags=["reservations"], status_code=200)
async def confirm_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return confirm_reservation_use_case(reservation_id=reservation_id, db=db)
