from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Sadece kullanıcı kendisine ait verilere erişebilir.
    Admin tüm verilere erişebilir.
    """
    def has_object_permission(self, request, view, obj):
        # Admin ise tüm verilere erişebilir
        if request.user.is_staff:
            return True
        # Kullanıcı sadece kendi bilgisine erişebilir
        return obj == request.user
