from django.contrib import admin
from django.urls import path, include
from rest_framework.generics import ListAPIView
from rest_framework_swagger.views import get_swagger_view

from api.views import SearchListView

app_name = 'search'

urlpatterns = [
    path('search/',SearchListView.as_view() ),

]
