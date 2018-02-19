"""
Fonzie, Open edX API

Endpoint: /status
Purpose: views related to the API status
"""
from __future__ import absolute_import, unicode_literals

from rest_framework.response import Response
from rest_framework.views import APIView

from fonzie import __version__ as fonzie_version


class VersionView(APIView):
    """API version

    Endpoint: /version
    Purpose: get the running release
    """

    # pylint: disable=redefined-builtin
    def get(self, request, format=None):
        """API version is read-only"""

        return Response({'version': fonzie_version})
