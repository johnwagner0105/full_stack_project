from rest_framework import serializers
from .models import AreasModel, CargosModel, UsuarioModel, loginModel


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasModel
        fields = "__all__"


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargosModel
        fields = "__all__"


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = "__all__"


class MostrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        exclude = ['password', 'is_staff',
                   'user_permissions', 'groups', 'last_login', 'is_superuser']


class RegistroLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = loginModel
        fields = "__all__"
