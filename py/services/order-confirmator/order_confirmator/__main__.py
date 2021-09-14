import asyncio
import json

import httpx
from aiokafka import AIOKafkaConsumer
from schemas.payment import PaymentConfirmed

from . import settings


def _deserializer(serialized):
    return json.loads(serialized)


async def _consume_payment_messages():
    client = httpx.AsyncClient()
    consumer = AIOKafkaConsumer(
        "payment-confirmed", bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS, group_id=settings.KAFKA_GROUP_ID, value_deserializer=_deserializer,
        auto_offset_reset='earliest'
    )

    await consumer.start()

    try:
        async for msg in consumer:
            # TODO: deserialize depending on Kafka topic
            payment_confirmed = PaymentConfirmed(**msg.value)
            await client.post(f"{settings.ORDERS_URL}/orders/{payment_confirmed.order_id}/confirm/")
    finally:
        await consumer.stop()
        await client.aclose()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_consume_payment_messages())


if __name__ == "__main__":
    main()
