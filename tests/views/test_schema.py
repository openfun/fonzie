# -*- coding: utf-8 -*-
"""
Tests for the `fonzie` models module.
"""

from __future__ import absolute_import, unicode_literals

from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from django.urls import reverse


class FonzieSchemaViewTestCase(APITestCase):
    """Tests for the FonzieSchemaView"""

    def setUp(self):
        """
        Initalize custom attributes:

        * client: the DRF RequestClient (requests wrapper)
        * url: target view fully qualified URL (required for requests)
        """

        self.url = 'http://{}{}'.format(
            'localhost',
            reverse('schema:schema', kwargs={'version': '1.0'})
        )
        self.client = RequestsClient()

    def test_get(self):
        """
        A GET request should return the API schema in the following formats:

        * coreapi (default)
        * openapi
        """
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.headers.get('Content-Type') == 'application/coreapi+json'

        headers = {'Accept': 'application/openapi+json'}
        response = self.client.get(self.url, headers=headers)
        assert response.status_code == status.HTTP_200_OK
        assert response.headers.get('content-type') == 'application/openapi+json'
