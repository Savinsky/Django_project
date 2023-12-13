from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

"""
class IsAuthenticated_CUSTOM(BasePermission):
    def has_permission(self, request, view):
        # ----------------------------
        # Ваши условия!
        if request.user.is_authenticated:


        #----------------------------
            return True
        return False
"""