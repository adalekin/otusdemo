import datetime

from schemas.payment import PaymentConfirmed
from sqlalchemy.orm import Session

from payments import models, schemas
from payments.db.utils import transaction
from payments.exceptions import PaymentNotFound
from payments.kafka import producer
from payments.models.payment import PaymentStatus


def create_payment_use_case(create_payment: schemas.CreatePayment, db: Session):
    now = datetime.datetime.utcnow()

    with transaction(db):
        payment = models.Payment(**create_payment.dict(), status=PaymentStatus.created, updated_at=now, created_at=now)

        db.add(payment)

    return schemas.Payment.from_orm(payment)


async def confirm_payment_use_case(payment_id: int, db: Session):
    with transaction(db):
        payment = db.query(models.Payment).filter(models.Payment.id == payment_id).one_or_none()

        if not payment:
            raise PaymentNotFound()

        payment.status = PaymentStatus.confirmed
        db.add(payment)

    payment_confirmed = PaymentConfirmed(**schemas.Payment.from_orm(payment).dict())
    await producer.send("payment-confirmed", payment_confirmed.json())

    return schemas.Payment.from_orm(payment)
