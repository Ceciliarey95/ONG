from django.urls import path
from . import views

app_name = 'apps.comentario'

urlpatterns = [
    path('addComentario/', views.AddComentario,name="addComentario"),
    path('comentarios/', views.Comentarioss, name="comentarios"),
    path('deleteComentario/<pk>', views.DeleteComentario.as_view(),name="eliminarComentario"),
]