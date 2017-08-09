# -*- coding: utf-8 -*-
__author__ = 'lateink'
from django.conf.urls import url
from django.views import static
from views import get_index, fetch


urlpatterns = [
    url(r'^$', get_index, name='index'),
    url(r'^fetch/$', fetch, name='fetch'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'static'}),
]