import environs

ENV = environs.Env()
ENV.read_env(".env")

ORDERS_URL = ENV("ORDERS_URL")

# KAFKA CONFIGURATION
KAFKA_BOOTSTRAP_SERVERS = ENV.list("KAFKA_BOOTSTRAP_SERVERS", default=["127.0.0.1:9092"])
KAFKA_GROUP_ID = ENV("KAFKA_GROUP_ID", "order-confirmator")
