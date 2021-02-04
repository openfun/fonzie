# coding: utf-8
"""
API user views
"""

from __future__ import absolute_import, unicode_literals

from datetime import datetime

import jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings


class UserSessionView(APIView):
    """API endpoint to get the authenticated user information."""

    permission_classes = [IsAuthenticated]

    # pylint: disable=redefined-builtin
    def get(self, request, version, format=None):
        """
        Retrieve logged in user, then generate a JWT with a claim containing its
        username (unique identifier) and its email. The token's expiration is
        synchronized with the user session expiration date.
        """
        user = request.user
        issued_at = datetime.utcnow()
        expired_at = request.session.get_expiry_date()
        token = jwt.encode(
            {
                "email": user.email,
                "username": user.username,
                "exp": expired_at,
                "iat": issued_at,
            },
            getattr(settings, "JWT_PRIVATE_SIGNING_KEY", None),
            algorithm="HS256",
        )

        return Response(
            {
                "access_token": token,
                "username": user.username,
            }
        )
