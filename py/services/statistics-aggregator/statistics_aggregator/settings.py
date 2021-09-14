import environs

ENV = environs.Env()
ENV.read_env(".env")

# CASSANDRA CONFIGURATION
CASSANDRA_CONTACT_POINTS = ENV.list("CASSANDRA_CONTACT_POINTS")
CASSANDRA_PORT = ENV("CASSANDRA_PORT", default=9042)
CASSANDRA_KEYSPACE = ENV("CASSANDRA_KEYSPACE", default="statistics")
CASSANDRA_USERNAME = ENV("CASSANDRA_USERNAME", default="cassandra")
CASSANDRA_PASSWORD = ENV("CASSANDRA_PASSWORD", default="")

# KAFKA CONFIGURATION
KAFKA_BOOTSTRAP_SERVERS = ENV.list("KAFKA_BOOTSTRAP_SERVERS", default=["127.0.0.1:9092"])
KAFKA_GROUP_ID = ENV("KAFKA_GROUP_ID", "statistics-aggregator")
