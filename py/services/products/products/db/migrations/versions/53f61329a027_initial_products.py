"""Initial products

Revision ID: 53f61329a027
Revises: 7a43b39f9fda
Create Date: 2021-09-12 16:12:04.008036

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "53f61329a027"
down_revision = "651bc5879202"
branch_labels = None
depends_on = None


def upgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=("products",))

    products = sa.Table("products", meta)

    op.bulk_insert(
        products,
        [
            {"name": "iPhone 12 Pro", "price": 99900, "price_currency": "USD", "quantity": 100},
            {"name": "iPhone 12", "price": 79900, "price_currency": "USD", "quantity": 100},
            {"name": "iPhone SE", "price": 54900, "price_currency": "USD", "quantity": 100},
            {"name": "iPhone 11", "price": 74900, "price_currency": "USD", "quantity": 100},
            {"name": "iPhone XR", "price": 54900, "price_currency": "USD", "quantity": 100},
        ],
    )


def downgrade():
    pass
