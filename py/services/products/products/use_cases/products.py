from sqlalchemy.orm import Session
from sqlalchemy.util.compat import print_

from products import models, schemas


def list_products_user_case(db: Session):
    for product in db.query(models.Product).all():
        yield schemas.Product.from_orm(product)
