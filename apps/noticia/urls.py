from django.urls import path
from . import views
app_name = 'apps.noticia'


urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view(),name="addNoticia"),#Listo
    path('addCategoria/', views.AddCategoria.as_view(),name="addCategoria"),#Listo
    path('listarNoticia2/', views.ListarNoticia, name="listarNoticia2"),#Listo
    path('listarPorCategoria/<str:categoria>',views.ListarNoticiaPorCategoria, name='listarPorCategoria'),#Listo
    path('readpost/<int:id>', views.ReadPost, name="readpost"),#Listo
    path('eliminarNoticia/<pk>', views.DeleteNoticia.as_view(),name="eliminarNoticia"),#Listo
    path('modificarNoticia/<pk>', views.UpdateNoticia.as_view(), name="modificarNoticia"), #Listo
]