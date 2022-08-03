from django.urls import path
from . import views
app_name = 'apps.noticia'


urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view()),
    path('listaNoticia/',views.MostrarNoticia.as_view()),
    path('listaNoticia2/', views.ListarNoticia),
    path('listarCategoria/<str:categoria>',views.ListarNoticiaPorCategoria, name='listarCategoria'),
]