from django.urls import path
from . import views
from .views import PostDetailView, ListarNoticia
app_name = 'apps.noticia'


urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view(),name="addNoticia"),
    path('listarNoticia/',views.MostrarNoticia.as_view(), name="listarNoticia"),
    path('listarNoticia2/', views.ListarNoticia, name="listarNoticia2"),
    path('listarCategoria/<str:categoria>',views.ListarNoticiaPorCategoria, name='listarCategoria'),
    path('post-detail/', PostDetailView.as_view(), name='post-detail'),
    #path('like/', views.AddLike.as_view(), name='like' ),
    #path('dislike/', views.AddDislike.as_view(), name='dislike' ),
]