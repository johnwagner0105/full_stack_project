from rest_framework import generics, response, status, request, permissions
from .models import AreasModel, CargosModel, UsuarioModel, loginModel
from .serializers import AreaSerializer, CargoSerializer, RegistroUsuarioSerializer, MostrarUsuarioSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken
from datetime import datetime
# Create your views here.


class AreaApiView(generics.ListCreateAPIView):
    queryset = AreasModel.objects.all()
    serializer_class = AreaSerializer


class CargoApiView(generics.ListCreateAPIView):
    queryset = CargosModel.objects.all()
    serializer_class = CargoSerializer
    # print(queryset[0].area.id)


class RegistroUsuarioApiView(generics.CreateAPIView):
    def post(self, request: request.Request):
        serializador = RegistroUsuarioSerializer(data=request.data)
        if serializador.is_valid():
            nuevo_usuario = UsuarioModel(**serializador.validated_data)
            nuevo_usuario.set_password(
                serializador.validated_data.get('password'))

            nuevo_usuario.save()
            return response.Response(data={
                'message': 'Usuario creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            return response.Response(data={
                'message': 'Error al registrar el usuario',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class PerfilUsuarioApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: request.Request):
        print(request.user)
        print(request.auth)

        usuario_encontrado = MostrarUsuarioSerializer(instance=request.user)

        return response.Response(data={
            'content': usuario_encontrado.data
        })


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('access')
        decoded_token = AccessToken(token)
        user_id = decoded_token['user_id']

        user = UsuarioModel.objects.get(id=user_id)

        login = loginModel.objects.create(
            date=datetime.now(),
            # date=datetime.now().strftime('%Y-%m-%d'),
            usuario=user
        )

        login.save()

        return response
