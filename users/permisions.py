from rest_framework.permissions import BasePermission

class IsActive(BasePermission):
    """permission для определения является ли пользователь активным"""
    def has_permission(self, request, view):
        return request.user.is_active
