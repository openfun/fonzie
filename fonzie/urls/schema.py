# -*- coding: utf-8 -*-
"""
Open/Core API schema endpoint
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from ..apps import FonzieConfig
from ..views.schema import FonzieSchemaView

app_name = FonzieConfig.name
urlpatterns = [
    url(
        r'^$',
        FonzieSchemaView.as_view(title="Fonzie, an Open API for Open edX"),
        name='schema'
    ),
]
