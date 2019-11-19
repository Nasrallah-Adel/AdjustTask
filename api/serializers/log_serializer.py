from rest_framework import serializers

from api.models import Logs


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue')
