# from rest_framework.permissions import BasePermission, SAFE_METHODS
#
#
# class IsSalesmanOrReadOnly(BasePermission):
#
#     def has_permission(self, request, view):
#         if request.method in ['POST', 'PATCH', 'PUT'] and request.user.type == 'salesman':
#             return True
#         return True


