# -*- coding: utf-8 -*-
"""
Tests for the `fonzie` views module.
"""

from __future__ import absolute_import, unicode_literals

from rest_framework import status  # pylint: disable=import-error
from rest_framework.test import APITestCase  # pylint: disable=import-error

from django.core.urlresolvers import reverse

from fonzie import __version__ as fonzie_version


class VersionViewTestCase(APITestCase):
    """Tests for the Versionview"""

    def setUp(self):
        """Set view url"""
        super(VersionViewTestCase, self).setUp()

        self.url = reverse("fonzie:status:version", kwargs={"version": "1.0"})

    def test_get(self):
        """HTTP/GET returns API version"""

        response = self.client.get(self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, {"version": fonzie_version})

    def test_post(self):
        """HTTP/POST should return a 405"""

        response = self.client.post(self.url, data={}, format="json")

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
