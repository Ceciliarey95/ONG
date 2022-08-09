from django.urls import path
from . import views
app_name = 'apps.noticia'


urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view(),name="addNoticia"),
    path('listaNoticia/',views.MostrarNoticia.as_view(), name="listarNoticia"),
    path('listaNoticia2/', views.ListarNoticia, name="listarNoticia2"),
    path('listarCategoria/<str:categoria>',views.ListarNoticiaPorCategoria, name='listarCategoria'),
]