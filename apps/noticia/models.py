from audioop import reverse
from django.db import models
from django.utils import timezone
from apps.usuario.models import Usuario

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
    imagen    = models.ImageField(upload_to='noticia', default='noticia/default.png')
    published = models.DateTimeField(default=timezone.now)
    likes     = models.ManyToManyField(Usuario, related_name = 'post_likes')
    

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.titulo

    
    #like = models.ManyToManyField(Usuario, blank=True,related_name='likes')
    #dislike = models.ManyToManyField(Usuario, blank=True,related_name='dislikes')

#__________Creado desde 0 en youtube__________#


