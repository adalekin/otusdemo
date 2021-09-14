from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from deeplinks import settings


class Deeplink(Model):
    __keyspace__ = settings.CASSANDRA_KEYSPACE

    user_id = columns.Integer(primary_key=True, required=True)
    id = columns.Text(primary_key=True, required=True)
    url = columns.Text(required=True)
    cn = columns.Text()
    cs = columns.Text()
