from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

app_name = 'api'
schema_view = get_swagger_view(title='api')
urlpatterns = [
    path('api/', include('api.urls', namespace='search')),

    path('', schema_view),
]
