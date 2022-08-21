from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

#from .views import
app_name = 'apps.usuario'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="usuario/login.html"),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('addUsuario/', views.RegistrarUsuario.as_view(),name="addUsuario"),
]