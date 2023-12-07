# coding: utf-8
"""
API user views
"""
# pylint: disable=import-error
from __future__ import absolute_import, unicode_literals

from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from openedx.core.lib.api.authentication import SessionAuthenticationAllowInactiveUser


class UserSessionView(APIView):
    """API endpoint to get the authenticated user information."""

    authentication_classes = [SessionAuthenticationAllowInactiveUser]
    permission_classes = [IsAuthenticated]

    # pylint: disable=redefined-builtin
    def get(self, request, version, format=None):
        """
        Retrieve logged in user, then generate a JWT with a claim containing its
        username (unique identifier) and its email. The token's expiration can
        be changed through the setting `ACCESS_TOKEN_LIFETIME` (default 5 minutes).
        """
        user = request.user
        issued_at = datetime.utcnow()
        try:
            language = user.preferences.get(key="pref-lang").value
        except ObjectDoesNotExist:
            language = settings.LANGUAGE_CODE
        token = AccessToken()
        token.payload.update(
            {
                "email": user.email,
                "full_name": user.profile.name,
                "iat": issued_at,
                "language": language,
                "username": user.username,
                "is_active": user.is_active,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser,
            },
        )

        return Response(
            {
                "access_token": str(token),
                "username": user.username,
                "full_name": user.profile.name,
            }
        )
