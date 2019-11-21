from django.db.models import Sum, FloatField
from django.db.models.functions import Cast
from django_filters import Filter, FilterSet, filters

from api.models import Logs


class GroupByFilter(Filter):
    def filter(self, qs, values):
        try:
            values = list(values.split(','))
        except:
            return qs
        if values is None:
            return qs
        return qs.values(*values).order_by()


class AnnotateFilter(Filter):
    def filter(self, qs, values):
        if values is None:
            return qs
        filter = {val: Sum(val) for val in values.split(',')}
        return qs.order_by().annotate(**filter)


class CpiFilter(Filter):
    def filter(self, qs, value):
        if value:
            return qs.order_by().annotate(CPI=Cast(Sum('spend') / Sum('installs'), FloatField()))
        return qs


class LogFilter(FilterSet):
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte')
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte')
    channel = filters.CharFilter(field_name='channel', lookup_expr='exact')

    country = filters.CharFilter(field_name='country', lookup_expr='exact')
    os = filters.CharFilter(field_name='os', lookup_expr='exact')

    groupby = GroupByFilter()
    CPI = CpiFilter()
    annotate = AnnotateFilter()


    class Meta:
        model = Logs
        fields = ['date_from', 'date_to', 'channel', 'country', 'os']
