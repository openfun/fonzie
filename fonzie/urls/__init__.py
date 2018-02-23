# -*- coding: utf-8 -*-
"""
URLs for fonzie.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from ..apps import FonzieConfig
from . import schema as schema_urls
from . import status as status_urls
from . import students as students_urls

app_name = FonzieConfig.name

API_PREFIX = r'^v(?P<version>[0-9]+\.[0-9]+)'

urlpatterns = [
    url(r'{}/schema/'.format(API_PREFIX), include(schema_urls, namespace='schema')),
    url(r'{}/status/'.format(API_PREFIX), include(status_urls, namespace='status')),
    url(r'{}/students/'.format(API_PREFIX), include(students_urls, namespace='students')),
]
