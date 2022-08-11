from audioop import reverse
import email
from django.db import models
#from apps.comentario.models import ComentariosManager, Comentarios
from django.contrib.contenttypes.models import ContentType
#from django.core.urlresolvers import reverse 
from apps.usuario.models import Usuario
#from tinymce.models import HTMLField
from django.utils import timezone


class Categoria(models.Model):
    nombre = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft','Draft'),
        ('published', 'Published')
    )

    titulo    = models.CharField(max_length=250, null=False)
    subtitulo = models.TextField(null=True)
    fecha     = models.DateTimeField(auto_now_add=True)
    texto     = models.TextField(null=False)
    activo    = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen    = models.ImageField(upload_to='noticia', default='noticia/default.png')
    published = models.DateTimeField(default=timezone.now)
    slug      = models.SlugField(max_length=250, unique_for_date='published', null=False,unique=True)
    status    = models.CharField(max_length=10, choices=options, default='draft')
    objects   = models.Manager()
    postobjects= PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.titulo

    
class Comment(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comments')
    name    = models.CharField(max_length=50)
    email   = models.EmailField()
    texto   = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status  = models.BooleanField(default=True)

    class Meta:
        ordering = ('-publish',)

        def __str__(self):
            return f'Comentario de {self.name}'
    
    #like = models.ManyToManyField(Usuario, blank=True,related_name='likes')
    #dislike = models.ManyToManyField(Usuario, blank=True,related_name='dislikes')
"""
    def __unicode__(self):
        return self.slug

    #def get_absolute_url(self):
    #    return reverse("post_idd", kwargs={"pk": self.pk})

    def comentarios(self):
        instance = self
        qs = Comentarios.objects.filtro_por_instancia(instance)
        return qs

    def get_content_type(self):
        content_type = ContentType.objects.get_for_model(Noticia)
        return content_type"""

#__________Creado desde 0 en youtube__________#


