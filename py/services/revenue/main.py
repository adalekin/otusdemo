import asyncio
import json

import aiohealthcheck
import httpx
from aiokafka import AIOKafkaConsumer
from aiorun import run
from schemas.event import EventFired

from revenue import settings


def _deserializer(serialized):
    return json.loads(serialized)


async def _get_account_id_by_user_id(client, user_id):
    response = await client.get(f"{settings.BILLING_URL}/accounts/find_by_user_id/{user_id}/")

    if response.status_code != 200:
        return None

    return response.json()["id"]


async def _consume_event_fired():
    client = httpx.AsyncClient()
    consumer = AIOKafkaConsumer(
        "event-fired",
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id=settings.KAFKA_GROUP_ID,
        value_deserializer=_deserializer,
        auto_offset_reset="earliest",
    )

    await consumer.start()

    try:
        async for msg in consumer:
            event_fired = EventFired(**msg.value)

            if event_fired.ec != "revenue":
                continue

            account_id = await _get_account_id_by_user_id(client=client, user_id=event_fired.partner_id)

            await client.post(
                f"{settings.BILLING_URL}/balance_transactions/",
                json={"account_id": account_id, "type": "charge", "amount": event_fired.ev, "currency": "USD"},
            )
    finally:
        await consumer.stop()
        await client.aclose()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.create_task(aiohealthcheck.tcp_health_endpoint(port=5000))
    loop.create_task(_consume_event_fired())

    run(loop=loop, stop_on_unhandled_errors=True)
