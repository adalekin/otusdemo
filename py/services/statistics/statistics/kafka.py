from aiokafka import AIOKafkaProducer

from . import settings

producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
