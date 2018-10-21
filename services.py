import models


def fetch_district_names(district_ids):
    districts = models.db_session.query(models.District) \
        .filter(models.District.id.in_(district_ids)) \
        .all()

    return [district.name for district in districts]