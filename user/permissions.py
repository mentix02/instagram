from django.contrib.auth import get_user_model

from rest_framework import permissions

User = get_user_model()


class UserIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'user') and isinstance(obj.user, User):
            return obj.user.id == request.user.id
        else:
            return obj.id == request.user.id
