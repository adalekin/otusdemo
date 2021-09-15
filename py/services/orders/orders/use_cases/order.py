from talepy import run_transaction

from orders.sagas.affo import SendEvent
from orders.sagas.order import CreateOrder, CompleteOrder


def create_order_use_case(user_id, items, tid=None, cid=None, cn=None, cs=None):
    state = run_transaction(
        steps=[CreateOrder(), SendEvent(), CompleteOrder(), SendEvent()],
        starting_state={"user_id": user_id, "items": items, "tid": tid, "cid": cid, "cn": cn, "cs": cs},
    )

    return state["order"]
