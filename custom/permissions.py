from rest_framework import permissions


class IsDoctor(permissions.BasePermission):
    message = 'Only doctors can access this resource'

    def has_permission(self, request, view):
        return bool(request.user.is_doctor)
