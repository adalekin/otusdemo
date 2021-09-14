import datetime

from sqlalchemy.orm import Session

from products import models, schemas
from products.db.utils import transaction
from products.exceptions import OutOfStock, ProductNotFound, ReservationNotFound
from products.models.reservation import ReservationStatus


def create_reservation_use_case(create_reservation: schemas.CreateReservation, db: Session):
    now = datetime.datetime.utcnow()

    with transaction(db):
        product = db.query(models.Product).filter(models.Product.id == create_reservation.product_id).one_or_none()

        if not product:
            raise ProductNotFound()

        if product.quantity < create_reservation.quantity:
            raise OutOfStock()

        product.quantity = product.quantity - create_reservation.quantity

        reservation = models.Reservation(
            **create_reservation.dict(), status=ReservationStatus.created, updated_at=now, created_at=now
        )

        db.add(reservation)
        db.add(product)

    return schemas.Reservation.from_orm(reservation)


def confirm_reservation_use_case(reservation_id: int, db: Session):
    with transaction(db):
        reservation = db.query(models.Reservation).filter(models.Reservation.id == reservation_id).one_or_none()

        if not reservation:
            raise ReservationNotFound()

        reservation.status = ReservationStatus.confirmed
        db.add(reservation)

    return schemas.Reservation.from_orm(reservation)
