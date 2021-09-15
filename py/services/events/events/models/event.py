from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from events import settings


class Event(Model):
    __keyspace__ = settings.CASSANDRA_KEYSPACE

    # Hit
    t = columns.Text(required=True)
    partner_id = columns.Integer(primary_key=True, required=True)
    tid = columns.Text(required=True)
    cid = columns.Text(required=True)
    created_at = columns.DateTime(primary_key=True)

    cf1 = columns.Text()
    cf2 = columns.Text()
    cf3 = columns.Text()
    cf4 = columns.Text()
    cf5 = columns.Text()
    # Traffic Sources
    dr = columns.Text()
    cn = columns.Text()
    cs = columns.Text()
    # Content Information
    dl = columns.Text()
    dh = columns.Text()
    # Session
    uip = columns.Text()
    uua = columns.Text()
    # Event
    ec = columns.Text()
    ea = columns.Text()
    el = columns.Text()
    ev = columns.Integer()
