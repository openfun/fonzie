# coding: utf-8
"""
API user endpoints
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from ..apps import FonzieConfig
from ..views.user import UserSessionView

app_name = FonzieConfig.name
urlpatterns = [url(r"^me/?$", UserSessionView.as_view(), name="me")]
