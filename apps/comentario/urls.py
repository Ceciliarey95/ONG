from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'apps.comentario'

urlpatterns = [
    path('comentar/', views.AddComentario.as_view(),name="addComentario"),
    #path('listarNoticia/', views.MostrarComentario.as_view()),
    path('post_id/', views.post_idd, name='post_idd'),
    path('comentario_id/', views.comentario_id, name='comentario_id'),
]