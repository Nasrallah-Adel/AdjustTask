from django_filters import Filter, FilterSet, filters

from api.models import Logs


class LogFilter(FilterSet):

    date_mx = filters.DateFilter(field_name='date', lookup_expr='lte')
    date_mn = filters.DateFilter(field_name='date', lookup_expr='gte')
    channel = filters.CharFilter(field_name='channel', lookup_expr='exact')

    country = filters.CharFilter(field_name='category__id', lookup_expr='exact')
    os = filters.CharFilter(field_name='category__id', lookup_expr='exact')

    class Meta:
        model = Logs
        fields = ['date_mx','date_mn', 'channel', 'country', 'os']
