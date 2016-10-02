from django.conf.urls import url
from django.contrib import admin

from .views import (areas_list)

urlpatterns = [
	url(r'^$',areas_list, name='list')
]