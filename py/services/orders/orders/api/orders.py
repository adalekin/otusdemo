from orders.models.order import order_schema
from orders.use_cases.order import create_order_use_case


def create(order):
    order_ = create_order_use_case(user_id=1, **order)

    return order_schema.dump(order_), 201
