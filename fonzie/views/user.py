# coding: utf-8
"""
API user views
"""

from __future__ import absolute_import, unicode_literals

from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken


class UserSessionView(APIView):
    """API endpoint to get the authenticated user information."""

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
        token = AccessToken()
        token.payload.update(
            {
                "email": user.email,
                "full_name": user.profile.name,
                "iat": issued_at,
                "username": user.username,
            },
        )

        return Response(
            {
                "access_token": str(token),
                "username": user.username,
            }
        )
