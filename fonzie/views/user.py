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
from django.utils.decorators import method_decorator

from openedx.core.lib.api.authentication import SessionAuthenticationAllowInactiveUser

# Since Hawthorn version, the module `cors_csrf` has been moved from `common.djangoapps`
# to `openedx.core.djangoapps`. So according to the version of Open edX, we need to
# import the module from the right place.
try:
    # First try to import the module from `openedx.core.djangoapps`
    from openedx.core.djangoapps.cors_csrf.decorators import ensure_csrf_cookie_cross_domain
except ImportError:
    # Otherwise, we are using an older version of Open edX, so we import the module
    # from `common.djangoapps`
    from cors_csrf.decorators import ensure_csrf_cookie_cross_domain


class UserSessionView(APIView):
    """API endpoint to get the authenticated user information."""

    authentication_classes = [SessionAuthenticationAllowInactiveUser]
    permission_classes = [IsAuthenticated]

    # To be able to update user profile through route api/user/v1/accounts/:username
    # we need to provide a valid CSRF Token. This is why we need to ensure that
    # the CSRF cookie is set for cross domain requests.
    @method_decorator(ensure_csrf_cookie_cross_domain)
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
