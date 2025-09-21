from rest_framework import permissions

class IsStaffOrAdmin(permissions.BasePermission):
    """
    Only users with role staff OR admin (or superuser) can modify create/update/delete.
    Read (GET) allowed for any.
    """
    def has_permission(self, request, view):
        # allow safe methods for everyone (or allow authenticated only if you prefer)
        if request.method in permissions.SAFE_METHODS:
            return True
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return getattr(user, 'role', None) in ('staff','admin') or user.is_superuser

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    For Subscription view: only owner (user) or admin/staff can view/update (depending).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user or (request.user.is_authenticated and (request.user.role in ('staff','admin') or request.user.is_superuser))
        # update/delete: only owner or admin
        return obj.user == request.user or (request.user.is_authenticated and (request.user.role in ('admin',) or request.user.is_superuser))
