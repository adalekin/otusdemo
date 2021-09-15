from cassandra.cqlengine.management import create_keyspace_simple, sync_table

from stats import models, settings
from stats.database import db

create_keyspace_simple(name=settings.CASSANDRA_KEYSPACE, replication_factor=1, connections=[str(db)])

sync_table(models.FunnelDaily, connections=[str(db)])
