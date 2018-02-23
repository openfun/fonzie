# -*- coding: utf-8 -*-
"""
Open/Core API schema endpoint
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from ..apps import FonzieConfig
from ..views.students import StudentListAPIView


app_name = FonzieConfig.name
urlpatterns = [
    url(r'^$', StudentListAPIView.as_view(), name='student_list'),
]
