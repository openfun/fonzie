# -*- coding: utf-8 -*-
"""
URLs for fonzie.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from ..apps import FonzieConfig
from . import acl as acl_urls
from . import status as status_urls

app_name = FonzieConfig.name

# For now, as DRF OpenAPI only supports URLPathVersioning, we prefix API root
# URL by the API release number. *This is a temporary solution*.
# See: https://github.com/limdauto/drf_openapi#4-constraints
#
# TODO: switch to AcceptHeaderVersioning
# http://www.django-rest-framework.org/api-guide/versioning/#acceptheaderversioning
API_PREFIX = r"^v(?P<version>[0-9]+\.[0-9]+)"

urlpatterns = [
    url(r"{}/status/".format(API_PREFIX), include(status_urls, namespace="status")),
    url(
        r"{}/acl/".format(API_PREFIX),
        include(acl_urls, namespace="acl"),
    ),
]
