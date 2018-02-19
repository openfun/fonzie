# -*- coding: utf-8 -*-
"""
URLs for fonzie.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from . import status as status_urls


urlpatterns = [
    url(r'status/', include(status_urls, namespace='status')),
]
