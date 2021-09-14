from typing import Optional
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit

from deeplinks import models
from deeplinks.use_cases.event import send_event_use_case
from deeplinks.use_cases.id import encode_id_use_case


def set_query_parameters(url: str, **kwargs):
    """Given a URL, set or replace a query parameter and return the
    modified URL.

    >>> set_query_parameters(url="http://example.com?foo=bar&biz=baz", params={"foo": "stuff"})
    "http://example.com?foo=stuff&biz=baz"

    """
    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = {**parse_qs(query_string), **kwargs}
    query_params = dict(filter(lambda x: x[1], query_params.items()))

    encoded_query_string = urlencode(query_params, doseq=True)

    return urlunsplit((scheme, netloc, path, encoded_query_string, fragment))


async def hit_use_case(
    id: str,
    client_id: str,
    client_user_ip: Optional[str],
    client_user_agent: Optional[str],
    document_referer: Optional[str],
):
    deeplink_orm = models.Deeplink.objects.filter(id=id).allow_filtering().first()

    if not deeplink_orm:
        return None

    tid = encode_id_use_case(deeplink_orm.user_id)

    await send_event_use_case(
        t="pageview", tid=tid, cid=client_id, dr=document_referer, uip=client_user_ip, uua=client_user_agent
    )

    return set_query_parameters(url=deeplink_orm.url, tid=tid, cid=client_id, cn=deeplink_orm.cn, cs=deeplink_orm.cs)
