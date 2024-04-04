from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the requesting user is the owner of the todo
        return obj.email == request.user.email


class IsTodoOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the requesting user is the owner of the todo
        return obj.user == request.user
