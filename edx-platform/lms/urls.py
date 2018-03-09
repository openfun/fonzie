"""
URLs for LMS
"""
from django.conf.urls import include, url

import debug_toolbar


urlpatterns = [
    url(r'^api/', include('fonzie.urls')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
