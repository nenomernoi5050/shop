from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^buy/$', buy, name='buy'),
	url(r'^popoln/$', popoln, name='popoln'),
	url(r'^success/$', success, name='success'),
	url(r'^fail/$', fail, name='fail'),
]
