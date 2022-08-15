from django.contrib import admin
from .models import Noticia, Categoria
# Register your models here.

@admin.register(Noticia)
class AuthorAdmin(admin.ModelAdmin):
    list_display        = ('titulo', 'id','activo','fecha', 'categoria')

admin.site.register(Categoria)

