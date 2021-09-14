from cassandra.cqlengine.management import create_keyspace_simple, sync_table

from statistics import models, settings
from statistics.database import db

create_keyspace_simple(name=settings.CASSANDRA_KEYSPACE, replication_factor=1, connections=[str(db)])

sync_table(models.Event, connections=[str(db)])
