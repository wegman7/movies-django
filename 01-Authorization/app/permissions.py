from rest_framework.permissions import BasePermission

class ReadMessagesPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.hasPermission('read:messages')

# class CustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         print(request.user.hasPermission('read:messages'))
#         return True