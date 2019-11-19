from django.db import models

# Create your models here.
from django.utils.timezone import now


class Logs(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateField(auto_created=True, default=now, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    channel = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    os = models.CharField(max_length=100, null=True, blank=True)
    impressions = models.IntegerField(null=True, blank=True)
    clicks = models.IntegerField(null=True, blank=True)
    installs = models.IntegerField(null=True, blank=True)
    spend = models.FloatField(null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'Logs'
