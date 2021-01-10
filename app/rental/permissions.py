from rest_framework import permissions
from django.utils.translation import gettext as _


class IsOwner(permissions.BasePermission):
    messages = _("Not an Owner")

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.owner
