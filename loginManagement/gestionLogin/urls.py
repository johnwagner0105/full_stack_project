from django.urls import path
from .views import AreaApiView, CargoApiView, RegistroUsuarioApiView, PerfilUsuarioApiView, LoginView, LoginPerAreaView, RegistroAreaView, RegistroCargoView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('area', AreaApiView.as_view()),
    path('cargo', CargoApiView().as_view()),
    path('registro', RegistroUsuarioApiView.as_view()),
    path('login', LoginView.as_view()),
    path('perfil', PerfilUsuarioApiView.as_view()),
    path('busquedaporarea/<int:pk>', LoginPerAreaView.as_view()),
    path('creararea', RegistroAreaView.as_view()),
    path('crearcargo', RegistroCargoView.as_view())
]
