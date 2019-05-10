# -*- coding: utf-8 -*-
"""
Access control to instructor files API endpoint
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from ..apps import FonzieConfig
from ..views.acl import ReportView

app_name = FonzieConfig.name
urlpatterns = [
    url(
        r"^report/(?P<course_sha1>[a-f0-9]{40})/(?P<filename>[\d\w\-\_\.]+)$",
        ReportView.as_view(),
        name="report",
    )
]
