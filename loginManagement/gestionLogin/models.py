from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import UsuarioManager

# Create your models here.


class AreasModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100, unique=True, null=False)

    createdAt = models.DateTimeField(auto_now_add=True, db_column="created_at")
    updatedAt = models.DateTimeField(auto_now=True, db_column="updated_at")

    class Meta:
        db_table = "areas"


class CargosModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100, null=False)

    createdAt = models.DateTimeField(auto_now_add=True, db_column="created_at")
    updatedAt = models.DateTimeField(auto_now=True, db_column="updated_at")

    area = models.ForeignKey(
        to=AreasModel, on_delete=models.CASCADE, db_column="area_id")

    class Meta:
        db_table = "cargos"


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)
    cargo = models.ForeignKey(
        to=CargosModel, on_delete=models.CASCADE, db_column="cargo_id", default=1)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    createdAt = models.DateTimeField(auto_now_add=True, db_column="created_at")

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["nombre", "apellido"]

    objects = UsuarioManager()

    class Meta:
        db_table = "usuarios"


class loginModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateTimeField(null=False)
    usuario = models.ForeignKey(
        to=UsuarioModel, on_delete=models.CASCADE, db_column="usuario_id")

    class Meta:
        db_table = "login"
