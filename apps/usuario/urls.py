from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

#from .views import
app_name = 'apps.usuario'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="usuario/login.html"),name="login"),#Listo
    path('logout/', LogoutView.as_view(),name="logout"),#Listo
    path('addUsuario/', views.RegistrarUsuario.as_view(),name="addUsuario"),#Listo
    path('listarUsuarios/', views.Usuarios,name="listarUsuarios"),#Listo
    path('deleteUsuario/<pk>', views.DeleteUsuario.as_view(),name="eliminarUsuario"),#Listo
    path('modificarUsuario/<pk>', views.UpdateUsuario.as_view(), name="modificarUsuario"),
]