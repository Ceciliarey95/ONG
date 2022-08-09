from django.db import models
from apps.noticia.models import Noticia
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings

class ComentariosManager(models.Manager):
    def filtro_por_instancia(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id       = instance.id
        qs           = super(ComentariosManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


class Comentarios(models.Model):
    usuario         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    noticia         = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    texto           = models.TextField(verbose_name='Comentario')
    fecha           = models.DateTimeField(auto_now_add=True)
    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type','object_id')
    objects         = ComentariosManager()

    def __str__(self):
        return self.texto[:15]

    class Meta:
        ordering = ['-fecha']