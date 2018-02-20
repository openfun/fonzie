# -*- coding: utf-8 -*-
"""
Tests for the `fonzie` models module.
"""

from __future__ import absolute_import, unicode_literals

from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

from fonzie import __version__ as fonzie_version


class VersionViewTestCase(APITestCase):
    """Tests for the Versionview"""

    def setUp(self):
        """Set view url"""

        self.url = reverse('status:version')

    def test_get(self):
        """HTTP/GET returns API version"""

        response = self.client.get(self.url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'version': fonzie_version}

    def test_post(self):
        """HTTP/POST should return a 405"""

        response = self.client.post(self.url, data={}, format='json')
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
