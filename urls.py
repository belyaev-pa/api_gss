from django.conf.urls import url
from .views import *
app_name = 'api_gss'


urlpatterns = [
    url(r'^$', index, name='index'),
]