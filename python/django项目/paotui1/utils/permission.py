from rest_framework import permissions
from django.contrib.auth import get_user_model
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        User=get_user_model()
        if User=="UserAddress":
             return obj.useraddr == request.user
        elif User=="UserLeavingMessage":
            return obj.userlm == request.user
        elif User=="AlipayOrderSettle":
            return obj.useraos == request.user
        elif User=="UserAli":
            return obj.usera == request.user
        elif User=="OrderAccept":
            return obj.useroac == request.user



