from django.db import models

# Create your models here.
from django.utils.timezone import now


class Logs(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateField(auto_created=True, default=now, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'Logs'
