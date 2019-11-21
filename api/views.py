import django_filters
from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from api.FilterSets.log_set import LogFilter
from api.models import Logs
from api.serializers.log_serializer import LogSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    last_page_strings = ('last',)


class SearchListView(ListAPIView):
    # queryset = Logs.objects.all().order_by('id').distinct()
    queryset = Logs.objects.all().order_by('id').distinct()
    pagination_class = StandardResultsSetPagination
    serializer_class = LogSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, ]

    filter_class = LogFilter

    ordering_fields = ['date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue',
                       'CPI']
