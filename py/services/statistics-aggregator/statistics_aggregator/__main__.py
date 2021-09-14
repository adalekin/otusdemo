import asyncio
import datetime
import json

import httpx
from aiokafka import AIOKafkaConsumer

from . import models, settings
from .database import db


def _deserializer(serialized):
    return json.loads(serialized)


async def _consume_statistics_messages():
    client = httpx.AsyncClient()
    consumer = AIOKafkaConsumer(
        "pageview-statistics",
        "event-statistics",
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id=settings.KAFKA_GROUP_ID,
        value_deserializer=_deserializer,
        auto_offset_reset="earliest",
    )

    await consumer.start()

    try:
        async for msg in consumer:
            today = datetime.date.today()

            funnel_daily = models.FunnelDaily(partner_id=msg.value["partner_id"], date=today)

            if msg.topic == "pageview-statistics":
                funnel_daily.update(clicks=msg.value["clicks"])
            elif msg.topic == "event-statistics":
                funnel_daily.update(registrations=msg.value["registrations"], revenue=msg.value["revenue"])
    finally:
        await consumer.stop()
        await client.aclose()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_consume_statistics_messages())


if __name__ == "__main__":
    main()
