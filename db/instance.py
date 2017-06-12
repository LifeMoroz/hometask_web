from django.conf import settings

from db.db import SqlLiteFactory

db = SqlLiteFactory().get_db(settings.DB_PATH)
