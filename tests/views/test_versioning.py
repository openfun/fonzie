# -*- coding: utf-8 -*-
"""
Tests for the `fonzie` views module.
"""

from __future__ import absolute_import, unicode_literals

from rest_framework import status  # pylint: disable=import-error
from rest_framework.test import APITestCase  # pylint: disable=import-error

from django.core.urlresolvers import reverse

from fonzie import __version__ as fonzie_version


class VersioningSchemaTestCase(APITestCase):
    """Tests for the API versioning schema"""

    def setUp(self):
        """Set view url"""
        super(VersioningSchemaTestCase, self).setUp()

        self.url = reverse("fonzie:status:version", kwargs={"version": "1.0"})

    def test_url_path_versioning(self):
        """Test allowed API versions in URL Path API versioning"""

        # Default API version: 1.0
        url = reverse("fonzie:status:version", kwargs={"version": "1.0"})
        self.assertIn("v1.0", url)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, {"version": fonzie_version})

        # Unimplemented or forbidden API version
        url = reverse("fonzie:status:version", kwargs={"version": "1.1"})
        self.assertIn("v1.1", url)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertJSONEqual(
            response.content, {"detail": "Invalid version in URL path."}
        )
