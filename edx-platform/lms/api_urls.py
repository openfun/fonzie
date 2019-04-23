"""
URLs for fonzie
"""
from lms.urls import *

# Fonzie urls
urlpatterns += [
    url(r'^api/', include('fonzie.urls', namespace='fonzie')),
]
