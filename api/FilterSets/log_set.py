from django.db.models import Sum
from django_filters import Filter, FilterSet, filters

from api.models import Logs


class GroupByFilter(Filter):
    def filter(self, qs, values):
        try:
            values = list(values.split(','))
        except:
            return qs

        return qs.values(*values)


class AnnotateFilter(Filter):
    def filter(self, qs, values):
        if values is None:
            return qs
        filter = {val: Sum(val) for val in values.split(',')}
        return qs.order_by().annotate(**filter)


class LogFilter(FilterSet):
    date_mx = filters.DateFilter(field_name='date', lookup_expr='lte')
    date_mn = filters.DateFilter(field_name='date', lookup_expr='gte')
    channel = filters.CharFilter(field_name='channel', lookup_expr='exact')

    country = filters.CharFilter(field_name='country', lookup_expr='exact')
    os = filters.CharFilter(field_name='os', lookup_expr='exact')

    groupby = GroupByFilter()
    annotate = AnnotateFilter()

    class Meta:
        model = Logs
        fields = ['date_mx', 'date_mn', 'channel', 'country', 'os']
