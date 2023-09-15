from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user == obj.owner:
            return True


class IsSalesmanOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.type == 'salesman':
            return True
        if request.method in SAFE_METHODS:
            return True


