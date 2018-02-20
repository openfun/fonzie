# -*- coding: utf-8 -*-
"""
Fonzie, Open edX API

Base endpoint: /status
Purpose: get more info about running API
"""
from __future__ import absolute_import, unicode_literals

from rest_framework.response import Response
from rest_framework.views import APIView

from fonzie import __version__ as fonzie_version


class VersionView(APIView):
    """
    API endpoint to get running API version
    """

    # pylint: disable=redefined-builtin
    def get(self, request, version, format=None):
        """Retrieve API version (SemVer string)"""

        return Response({'version': fonzie_version})
