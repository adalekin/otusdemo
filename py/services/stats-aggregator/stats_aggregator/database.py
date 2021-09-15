from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection

from . import settings

auth_provider = PlainTextAuthProvider(username=settings.CASSANDRA_USERNAME, password=settings.CASSANDRA_PASSWORD)

db = Cluster(
    contact_points=settings.CASSANDRA_CONTACT_POINTS,
    port=settings.CASSANDRA_PORT,
    auth_provider=auth_provider,
).connect()

connection.register_connection(str(db), session=db)
connection.set_default_connection(str(db))
