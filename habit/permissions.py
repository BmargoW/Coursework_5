from rest_framework import permissions


class PublicOrCarrierPerm(permissions.BasePermission):
    """
        Разрешает доступ, если:
          - привычка публичная (publicity=True), ИЛИ
          - пользователь-носитель привычки (carrier)
        Работает только для авторизованных пользователей.
        """
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            if obj.publicity:
                return True

        return obj.carrier == request.user