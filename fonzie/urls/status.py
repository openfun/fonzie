# -*- coding: utf-8 -*-
"""
URLs for fonzie.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from ..views.status import VersionView

urlpatterns = [
    url(r'^version$', VersionView.as_view(), name='version'),
]
