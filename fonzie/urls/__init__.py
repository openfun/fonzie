# -*- coding: utf-8 -*-
"""
URLs for fonzie.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from ..apps import FonzieConfig
from . import status as status_urls

app_name = FonzieConfig.name
urlpatterns = [
    url(r'status/', include(status_urls, namespace='status')),
]
