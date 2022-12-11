from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Index, fotos, nosotros
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', Index, name='index'),
    path('noticia/', include('apps.noticia.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('comentario/', include('apps.comentario.urls')),
    path('fotos/', fotos, name='fotos'),
    path('nosotros/', nosotros, name='nosotros'),
    ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns() 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)