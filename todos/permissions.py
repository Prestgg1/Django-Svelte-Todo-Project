
from rest_framework.permissions import BasePermission
class IsTodoOwnerOrAdmin(BasePermission):
    """
    Sadece Todo sahibine veya adminlere izin verir.
    """
    def has_object_permission(self, request, view, obj):
        # Admin ise tüm verilere erişebilir
        if request.user.is_staff:
            return True
        # Kullanıcı sadece kendine ait todoları görebilir
        return obj.author == request.user
