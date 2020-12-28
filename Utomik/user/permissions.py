from rest_framework import permissions


PUBLIC_METHODS = ['GET', 'POST']

class isStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            return False
