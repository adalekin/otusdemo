from stats import models, schemas
from stats.database import db


def get_funnel_daily_use_case(user_id):
    for funnel_daily in models.FunnelDaily.objects.filter(partner_id=user_id).all():
        yield schemas.FunnelDaily.from_orm(funnel_daily)
