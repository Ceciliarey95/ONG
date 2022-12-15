from audioop import reverse
from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=250, null=False)
        
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo    = models.CharField(max_length=250, null=False)
    subtitulo = models.CharField(max_length=90, null=True, blank=True)
    fecha     = models.DateTimeField(auto_now_add=True)
    texto     = models.TextField(null=False) 
    activo    = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen    = models.ImageField(null=True, blank=True,upload_to='noticia', default='noticia/default.png')
    published = models.DateTimeField(default=timezone.now)  

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.titulo

