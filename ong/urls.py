from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView
#from django.conf.urls import url
"""urlpatterns = [
    url( r '^ tinymce /', include('tinymce.urls')),
]"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('noticia/', include('apps.noticia.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('comentario/', include('apps.comentario.urls')),
    path('reset/password_reset', PasswordResetView.as_view(), {'template_name':'password/password_reset_form.html', 'email_template_name': 'password/password_reset_email.html'}, name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(), {'template_name':'password/password_reset_done.html'}, name='password_reset_done'),
    #path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), {'template_name':'password/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('reset/password_reset_complet', PasswordResetCompleteView.as_view(), {'template_name':'password/password_reset_complete.html'}, name='password_reset_complete'),
    ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns() 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)