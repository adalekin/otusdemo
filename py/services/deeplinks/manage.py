from cassandra.cqlengine.management import create_keyspace_simple, sync_table

from deeplinks import models, settings
from deeplinks.database import db

create_keyspace_simple(name=settings.CASSANDRA_KEYSPACE, replication_factor=1, connections=[str(db)])

sync_table(models.Deeplink, connections=[str(db)])
