from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_superuser(self, email, nombre, apellido, password):
        if not email:
            raise ValueError("El usuario debe tener un correo")

        email_normalizado = self.normalize_email(email)
        nuevo_usuario = self.model(
            email=email_normalizado, nombre=nombre, apellido=apellido)
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()
