from audioop import reverse
from django.db import models
#from apps.comentario.models import ComentariosManager, Comentarios
from django.contrib.contenttypes.models import ContentType
#from django.core.urlresolvers import reverse 


class Categoria(models.Model):
    nombre = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.nombre



class Noticia(models.Model):
    titulo    = models.CharField(max_length=250, null=False)
    fecha     = models.DateTimeField(auto_now_add=True)
    texto     = models.TextField(null=False)
    activo    = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen    = models.ImageField(upload_to='noticia', default='noticia/default.png')
    #slug      = models.SlugField(unique=True, blank=True)

    def __unicode__(self):
        return self.slug

    #def get_absolute_url(self):
    #    return reverse("post_idd", kwargs={"pk": self.pk})

    """def comentarios(self):
        instance = self
        qs = Comentarios.objects.filtro_por_instancia(instance)
        return qs"""

    def get_content_type(self):
        content_type = ContentType.objects.get_for_model(Noticia)
        return content_type

    def __str__(self):
        return self.titulo