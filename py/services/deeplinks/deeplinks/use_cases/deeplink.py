from deeplinks.database import db
from deeplinks import models, schemas


def create_deeplink_use_case(user_id: int, create_deeplink: schemas.CreateDeeplink):
    deeplink = schemas.Deeplink(user_id=user_id, **create_deeplink.dict())
    deeplink_orm = models.Deeplink.create(**deeplink.dict())

    return schemas.Deeplink.from_orm(deeplink_orm)


def list_deeplinks_use_case(user_id: int):
    for deeplink_orm in models.Deeplink.objects.filter(user_id=user_id):
        yield schemas.Deeplink.from_orm(deeplink_orm)
