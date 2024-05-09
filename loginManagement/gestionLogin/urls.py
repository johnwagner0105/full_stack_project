from django.urls import path
from .views import AreaApiView, CargoApiView, RegistroUsuarioApiView, PerfilUsuarioApiView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('area', AreaApiView.as_view()),
    path('cargo', CargoApiView().as_view()),
    path('registro', RegistroUsuarioApiView.as_view()),
    path('login', LoginView.as_view()),
    path('perfil', PerfilUsuarioApiView.as_view())
]
