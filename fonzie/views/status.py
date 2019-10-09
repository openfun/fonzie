# -*- coding: utf-8 -*-
"""
API status views
"""
from __future__ import absolute_import, unicode_literals

from rest_framework.response import Response  # pylint: disable=import-error
from rest_framework.views import APIView  # pylint: disable=import-error

from fonzie import __version__ as fonzie_version


class VersionView(APIView):
    """API endpoint to get the running API version"""

    # pylint: disable=redefined-builtin
    def get(self, request, version, format=None):
        """Retrieve API version as a SemVer string"""
        return Response({"version": fonzie_version})
