"""
URLs for fonzie
This file appends Fonzie urls to edX lms urls.
It is intended to be defined in lms settings this way:

`ROOT_URLCONF = "fonzie.urls.lms_root"`
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from lms.urls import urlpatterns  # pylint: disable=import-error

# Fonzie urls
urlpatterns += [
    url(r"^api/", include("fonzie.urls", namespace="fonzie")),
]
