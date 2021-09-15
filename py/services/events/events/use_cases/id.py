from hashids import Hashids

from events import settings

HASHIDS = Hashids(salt=settings.HASHIDS_SALT, min_length=settings.HASHIDS_MIN_LENGTH)


def encode_id_use_case(id: int):
    return HASHIDS.encode(id)


def decode_id_use_case(id: str):
    return HASHIDS.decode(id)
