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
    '''
        get:
         search list

         - page : use page parameter if returned results big than 20 json object ---> (0:9)*\n
         - time range (date_from / date_to) date format ( yyy-mm-dd )\n
         ...........>* date_from : use grater than or equel >=\n
         ...........>* date_to : use less than or equel\n

         - channel : query parameter to search specific channel and it is case sensitive { adcolony - apple_search_ads - chartboost - facebook - ..... }\n
         - country : query parameter to search specific country and it is case sensitive { US - CA - DE - FR - ..... }\n
         - os : query parameter to search specific os and it is case sensitive { ios - android - ..... }\n



         - groupby  : is used to group by another fields { os , channel , country , date , .... }   and accept more
         than one value like  (os,channel) multi value separated by (,)\n
         - CPI : if you put it (true) will compute (cost per install) which is calculated as cpi = spend / installs\n
         - annotate : return sum of fields { installs,revenue,spend,clicks,impressions } accept more than one value like  (impressions,installs) multi value separated by (,)\n
         - ordering : you can order with fields ['date', 'channel', 'country', 'os', 'impressions', 'clicks',
         'installs', 'spend', 'revenue','CPI' ]  accept more than one value like  (impressions,installs) multi value
         separated by (,) if use just field name will be in asc order if use (-) before field will br in desc order \n


        NOTE : CPI and annotate work fine if group_by have value






    '''
    queryset = Logs.objects.all().order_by('id').distinct()
    pagination_class = StandardResultsSetPagination
    serializer_class = LogSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, ]

    filter_class = LogFilter

    ordering_fields = ['date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue',
                       'CPI']
