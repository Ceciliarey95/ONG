from django.urls import path
from . import views
app_name = 'apps.noticia'


urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view(),name="addNoticia"),
    path('addCategoria/', views.AddCategoria.as_view(),name="addCategoria"),
    path('listarNoticia2/', views.ListarNoticia, name="listarNoticia2"),
    path('listarPorCategoria/<str:categoria>',views.ListarNoticiaPorCategoria, name='listarPorCategoria'),
    path('readpost/<int:id>', views.ReadPost, name="readpost"),
    #path('eliminarNoticia/<int:id>', views.DeleteNoticia.as_view(),name="eliminarNoticia"),
]