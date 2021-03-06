import environs

ENV = environs.Env()
ENV.read_env(".env")

IP_ADDRESS_META_FIELD = ENV("IP_ADDRESS_META_FIELD", default="X-Forwarded-For")

# HASHIDS CONFIGURATION
HASHIDS_SALT = ENV("HASHIDS_SALT", default="90fce962aa905e94c22c97efbe7326d2")
HASHIDS_MIN_LENGTH = 6

# CASSANDRA CONFIGURATION
CASSANDRA_CONTACT_POINTS = ENV.list("CASSANDRA_CONTACT_POINTS")
CASSANDRA_PORT = ENV("CASSANDRA_PORT", default=9042)
CASSANDRA_KEYSPACE = ENV("CASSANDRA_KEYSPACE", default="deeplinks")
CASSANDRA_USERNAME = ENV("CASSANDRA_USERNAME", default="cassandra")
CASSANDRA_PASSWORD = ENV("CASSANDRA_PASSWORD", default="")

# EVENTS CONFIGURATION
EVENTS_URL = ENV("EVENTS_URL")

# DEEPLINKS CONFIGURATION
DEEPLINKS_BASE_URL = ENV("DEEPLINKS_BASE_URL", default="")
DEEPLINKS_TARGET_URL_TEMPLATE = ENV("DEEPLINKS_TARGET_URL_TEMPLATE", default=f"{DEEPLINKS_BASE_URL}/d/{{id}}")
