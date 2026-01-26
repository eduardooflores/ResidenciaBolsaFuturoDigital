from api.authentication import TokenAuthentication
from rest_framework import authentication, permissions

from api.permissions import FuturoPermissions


class BaseSecurity:
    authentication_classes = [TokenAuthentication, authentication.SessionAuthentication]

    permission_classes = [permissions.IsAuthenticated, FuturoPermissions    ]