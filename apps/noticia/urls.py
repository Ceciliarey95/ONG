from django.urls import path
from . import views
from .views import PostDetailView
app_name = 'apps.noticia'


urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view(),name="addNoticia"),
    path('listarNoticia/',views.MostrarNoticia.as_view(), name="listarNoticia"),
    path('listarNoticia2/', views.ListarNoticia, name="listarNoticia2"),
    path('listarPorCategoria/<str:categoria>',views.ListarNoticiaPorCategoria, name='listarPorCategoria'),
    path('post-detail/', PostDetailView.as_view(), name='post-detail'),
    path('modificarNoticia/<slug:slug>', views.ModificarNoticia.as_view(),name="modificarNoticia"),
    #path('like/', views.AddLike.as_view(), name='like' ),
    #path('dislike/', views.AddDislike.as_view(), name='dislike' ),
]