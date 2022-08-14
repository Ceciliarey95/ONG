from django.urls import path, re_path
from . import views
app_name = 'apps.noticia'


urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view(),name="addNoticia"),
    path('listarNoticia2/', views.ListarNoticia, name="listarNoticia2"),
    path('listarPorCategoria/<str:categoria>',views.ListarNoticiaPorCategoria, name='listarPorCategoria'),
    re_path(r'^listarFecha/(?P<fecha>[0-9]{4}-?[0-9]{2}-?[0-9]{2})', views.ListarNoticiaPorFecha, name="postFecha"),
    path('readpost/<int:id>', views.ReadPost, name="readpost"),
    #path('modificarNoticia/<int:id>', views.ModificarNoticia.as_view(),name="modificarNoticia"),
    #path('eliminarNoticia/<int:id>', views.DeleteNoticia.as_view(),name="eliminarNoticia"),
    #path('like/', views.AddLike.as_view(), name='like' ),
    #path('dislike/', views.AddDislike.as_view(), name='dislike' ),
]