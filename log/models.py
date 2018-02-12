from django.db import models


class Reading(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    battery_v = models.FloatField()
    pumping = models.FloatField()
    datetime = models.DateTimeField('date published')
