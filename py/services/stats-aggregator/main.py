import asyncio
import datetime
import json

import aiohealthcheck
import httpx
from aiokafka import AIOKafkaConsumer
from aiorun import run

from stats_aggregator import models, settings
from stats_aggregator.database import db


def _deserializer(serialized):
    return json.loads(serialized)


async def _consume_stats_messages():

    client = httpx.AsyncClient()

    consumer = AIOKafkaConsumer(
        "pageview-stats",
        "event-stats",
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

            if msg.topic == "pageview-stats":
                funnel_daily.update(clicks=msg.value["clicks"])
            elif msg.topic == "event-stats":
                funnel_daily.update(registrations=msg.value["registrations"], revenue=msg.value["revenue"])
    finally:
        await consumer.stop()
        await client.aclose()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.create_task(aiohealthcheck.tcp_health_endpoint(port=5000))
    loop.create_task(_consume_stats_messages())

    run(loop=loop)
