from unicodedata import name
from django.contrib import admin
from .models import Noticia, Categoria, Comment
# Register your models here.

@admin.register(Noticia)
class AuthorAdmin(admin.ModelAdmin):
    list_display        = ('titulo', 'id', 'status', 'slug')
    prepopulated_fields = {'slug': ('titulo',), }

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('noticia', 'name', 'email','publish','status')
    list_filter  = ('status', 'publish')
    search_fields= ('name','email','texto')



admin.site.register(Categoria)

