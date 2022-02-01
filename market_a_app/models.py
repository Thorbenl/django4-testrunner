from django.db import models
from django.db.models.fields.json import JSONField


class AdvertisementIdMapping(models.Model):
    advertisement_id = models.PositiveIntegerField(db_index=True, unique=True)


class MigratedMissingData(models.Model):
    instance_created_date = models.DateTimeField(auto_now_add=True)

    table = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    value = JSONField()
