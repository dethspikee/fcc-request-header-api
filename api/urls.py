from django.urls import path
from django.conf.urls import url

from .views import index, who_am_i


urlpatterns = [
    url(r'^api/whoami/?$', who_am_i),
    url(r'^$', index),
]