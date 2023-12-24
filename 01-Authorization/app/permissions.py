from rest_framework.permissions import BasePermission

class ReadMessagesPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.hasPermission('read:messages')

class ExamplePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.hasPermission('example:permission')