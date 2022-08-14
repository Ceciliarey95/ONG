from django.db import models
from apps.noticia.models import Noticia
from django.conf import settings



class Comentarios(models.Model):
    usuario         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    noticia         = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    texto           = models.TextField(verbose_name='Comentario')
    fecha           = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.texto

    class Meta:
        ordering = ['-fecha']