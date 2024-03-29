from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
from users import models, configurations

def is_authenticated(self, request, view):
    return IsAuthenticated.has_permission(self, request, view)

def is_user_permitted(request, role_name):
    if not request.user or request.user.is_staff:
        return False

    organization_role = models.Role.objects.filter(user__id=request.user.id, role=role_name).first()
    if organization_role is None:
        return False
    return True

class SamplePermissionUser(BasePermission):
    def has_permission(self, request, view):
        if not is_authenticated(self, request, view):
            return False
        if request.user.email == 'jithin.j@logicplum.com':
            return True
        else:
            return False


# class IsOrganizationAdmin(BasePermission):
#     """
#     Allows access only to organization admin users.
#     """
#     def has_permission(self, request, view):
#         if not is_authenticated(self, request, view):
#             return False
#         return is_user_permitted(request, configurations.ORGANIZATION_ADMIN)


# class IsOrganizationManager(BasePermission):
#     """
#     Allows access only to organization manager users.
#     """
#     def has_permission(self, request, view):
#         if not is_authenticated(self, request, view):
#             return False
#         return is_user_permitted(request, configurations.ORGANIZATION_MANAGER)


# class IsOrganizationScheduler(BasePermission):
#     """
#     Allows access only to organization executive users.
#     """
#     def has_permission(self, request, view):
#         if not is_authenticated(self, request, view):
#             return False
#         return is_user_permitted(request,configurations.ORGANIZATION_SCHEDULER)

# class IsOrganizationUser(BasePermission):
#     """
#     Allows access only to organization executive users.
#     """
#     def has_permission(self, request, view):
#         if not is_authenticated(self, request, view):
#             return False
#         return is_user_permitted(request,configurations.ORGANIZATION_USER)


# def is_user_allowed(request, role_name):
#     organization_role = models.Role.objects.filter(user__id=request.user.id, role=role_name)
#     if organization_role.exists():
#         return True
#     return False