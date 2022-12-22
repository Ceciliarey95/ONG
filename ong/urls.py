from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Index, fotos, nosotros, contacto
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', Index, name='index'),#Listo
    path('noticia/', include('apps.noticia.urls')),#Listo
    path('usuario/', include('apps.usuario.urls')),#Listo
    path('comentario/', include('apps.comentario.urls')),
    path('fotos/', fotos, name='fotos'),#Listo
    path('nosotros/', nosotros, name='nosotros'),#Listo
    path('contacto/', contacto, name='contacto'),#Listo
    ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns() 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)