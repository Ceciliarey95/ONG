from django.contrib import admin
from .models import Noticia, Categoria
# Register your models here.

@admin.register(Noticia)
class AuthorAdmin(admin.ModelAdmin):
    list_display        = ('titulo', 'id', 'status', 'slug')
    prepopulated_fields = {'slug': ('titulo',), }

admin.site.register(Categoria)

