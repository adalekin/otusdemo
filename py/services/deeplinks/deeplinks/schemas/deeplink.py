import random
from typing import Optional

from pydantic import BaseModel, Field, validator

from deeplinks import settings
from deeplinks.use_cases.id import encode_id_use_case


class CreateDeeplink(BaseModel):
    url: str
    cn: Optional[str] = None
    cs: Optional[str] = None


def _generate_id():
    int_ = random.getrandbits(64)

    id = encode_id_use_case(int_)

    # TODO: ensure it's not used
    return id


class Deeplink(CreateDeeplink):
    id: str = Field(default_factory=_generate_id)
    user_id: int
    target_url: Optional[str] = None

    class Config:
        orm_mode = True

    @validator("target_url", always=True)
    def ab(cls, v, values) -> str:
        return settings.DEEPLINKS_TARGET_URL_TEMPLATE.format(**values)
