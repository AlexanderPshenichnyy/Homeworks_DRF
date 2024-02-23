from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='moderator').exists():
            return True
        return obj.owner == request.user


class IsStaffOrOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().owner
