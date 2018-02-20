# -*- coding: utf-8 -*-
"""
URLs for fonzie.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from ..apps import FonzieConfig
from ..views.status import VersionView

app_name = FonzieConfig.name
urlpatterns = [
    url(r'^version$', VersionView.as_view(), name='version'),
]
