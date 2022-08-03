from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'apps.usuario'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'usuario/login.html'),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
]