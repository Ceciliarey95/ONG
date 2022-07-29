from django.db import models
from apps.noticia.models import Noticia
# Create your models here.

class Comentario(models.Model):

    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)