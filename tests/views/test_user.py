# coding: utf-8
"""
Tests for the `fonzie` user module.
"""

# pylint: disable=no-member,import-error
from __future__ import absolute_import, unicode_literals

import jwt
from rest_framework import status
from rest_framework.test import APITestCase

from django.core.urlresolvers import reverse
from django.test import override_settings

from openedx.core.djangoapps.user_api.tests.factories import UserPreferenceFactory
from student.tests.factories import UserFactory, UserProfileFactory


class UserViewTestCase(APITestCase):
    """Tests for the User API endpoint"""

    def setUp(self):
        """
        Set common parameters for the test suite.
        """
        super(UserViewTestCase, self).setUp()

        self.url = reverse("fonzie:user:me", kwargs={"version": "1.0"})

    def test_user_me_with_anonymous_user(self):
        """
        If user is not authenticated, view should return a 403 status
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @override_settings(LANGUAGE_CODE="de")
    def test_user_me_with_logged_in_user(self):
        """
        If user is authenticated through Django session, view should return
        a JSON object containing the username and a JWT access token
        """
        user = UserFactory.create(
            username="fonzie",
            email="arthur_fonzarelli@fun-mooc.fr",
        )
        UserProfileFactory.build(user=user, name="Arthur Fonzarelli")
        self.client.force_authenticate(user=user)

        response = self.client.get(self.url)
        token = jwt.decode(
            response.data["access_token"],
            "ThisIsAnExampleKeyForDevPurposeOnly",
            options={
                "require": ["email", "exp", "iat", "jti", "token_type", "username", "language"]
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "fonzie")
        self.assertEqual(token["username"], "fonzie")
        self.assertEqual(token["full_name"], "Arthur Fonzarelli")
        self.assertEqual(token["email"], "arthur_fonzarelli@fun-mooc.fr")
        # When the user has no language preference, LANGUAGE_CODE should be used
        self.assertEqual(token["language"], 'de')
        self.assertEqual(token["token_type"], "access")
        self.assertIsInstance(token["exp"], int)
        self.assertIsInstance(token["iat"], int)

    def test_user_me_with_logged_in_user_and_language_preference(self):
        """
        If user is authenticated through Django session, and it sets a language
        in its preferences, the JWT access token returned by the view should contain
        the language.
        """
        user = UserFactory.create(
            username="joanie",
            email="joanie_cunningham@fun-mooc.fr",
        )
        UserPreferenceFactory(user=user, key="pref-lang", value="fr")
        self.client.force_authenticate(user=user)

        response = self.client.get(self.url)
        token = jwt.decode(
            response.data["access_token"],
            "ThisIsAnExampleKeyForDevPurposeOnly",
            options={
                "require": ["email", "exp", "iat", "jti", "token_type", "username",
                            "language"]
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "joanie")
        self.assertEqual(token["email"], "joanie_cunningham@fun-mooc.fr")
        self.assertEqual(token["username"], "joanie")
        self.assertEqual(token["language"], "fr")
