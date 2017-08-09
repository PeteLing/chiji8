# -*- coding: utf-8 -*-
__author__ = 'lateink'

import os

DEBUG = os.environ.get('LEANCLOUD_APP_ENV') != 'production'
ROOT_URLCONF = 'urls'
SECRET_KEY = 'KD6X8apUraGzyPKoMByR8Y622'
ALLOWED_HOSTS = ['*']

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],
}]

LEAN_CLOUD_ID = 'zYX18V9C0G0EI8eg6cHe8k67-gzGzoHsz'
LEAN_CLOUD_SECRET = 'KD6X8apUraGzyPKoMByR8Y62'