
from pprint import pprint
from rest_framework import permissions
from management.utils.apicode import ApiCode

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

def method_permission_classes(classes):
    def decorator(func):
        def decorated_func(self, *args, **kwargs):
            self.permission_classes = classes
            # this call is needed for request permissions
            self.check_permissions(self.request)
            return func(self, *args, **kwargs)
        return decorated_func
    return decorator

class MyBasePermission(permissions.BasePermission):
    message = ApiCode.error(message="Bạn không có quyền để thực hiện hành động này")


class AllowAny(MyBasePermission):
    def has_permission(self, request, view):
        return True


class IsAuthenticated(MyBasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

class IsAdminUser(MyBasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_manager)


class IsAuthenticatedOrReadOnly(MyBasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

class IsSuperUser(MyBasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)

class IsOwnUserOrAdmin(MyBasePermission):
    def has_permission(self, request, view):
        return bool(request.user
            and request.user.is_authenticated
            and request.user.id == view.kwargs["id"]) or bool(
                request.user and request.user.is_manager)