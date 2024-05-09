from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission


class SoloAdministradorEnArea(BasePermission):
    def has_permission(self, request, view):
        # Obtenemos el ID del área desde la URL
        area_id_url = view.kwargs.get('pk')
        # print(area_id_url)
        if area_id_url is not None:
            print(request.user.cargo.area.id)
            # Comparamos el ID del área de la URL con el del usuario loggeado
            return request.user.cargo.area.id == int(area_id_url)
