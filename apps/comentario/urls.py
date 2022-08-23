from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'apps.comentario'

urlpatterns = [
    path('addComentario/', views.AddComentario,name="addComentario"),
    path('comentarios/', views.Comentarioss, name="comentarios"),
    
]