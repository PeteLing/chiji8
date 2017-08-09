# -*- coding: utf-8 -*-
__author__ = 'lateink'

import os

DEBUG = os.environ.get('LEANCLOUD_APP_ENV') != 'production'
ROOT_URLCONF = 'urls'
SECRET_KEY = 'KD6X8apUraGzyPKoMByR8Y622'
ALLOWED_HOSTS = ['jdqs.leanapp.cn']

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],
}]

LEAN_CLOUD_ID = 'WxX6D7TnJSfeaHYkP6f7DuYa-gzGzoHsz'
LEAN_CLOUD_SECRET = 'TA2ujuU7IezqselCKNf3TTwc'
