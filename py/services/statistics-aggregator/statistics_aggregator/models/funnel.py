from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from statistics_aggregator import settings


class FunnelDaily(Model):
    __keyspace__ = settings.CASSANDRA_KEYSPACE

    partner_id = columns.Integer(primary_key=True)
    clicks = columns.Integer(default=0)
    registrations = columns.Integer(default=0)
    revenue = columns.Integer(default=0)
    date = columns.Date(primary_key=True)
