#from http.client import HTTPResponse
from urllib import request
#from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Comentarios
from .forms import FormComentarios
from apps.noticia.models import Noticia
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect


def comentario_id(request,pk):
    instance = get_object_or_404(Noticia, pk=pk)
    context  ={
        "comentario":instance
    }
    return render(request, "comentario/instance.html",context)

class AddComentario(CreateView):
    model         = Comentarios
    fields        = ['autor', 'texto', 'fecha']
    template_name = 'usuario/comentario.html'


class MostrarComentario(ListView):
    model         = Comentarios
    template_name = 'usuario/mostrarComentario.html'

def post_idd(request, pk):
    instance = get_object_or_404(Noticia, pk=pk)

    inicializar_datos = {
        'content_type': instance.get_content_type,
        'object_id': instance.id
    }

    form= FormComentarios(request.POST or None, initial=inicializar_datos)

    if form.is_valid():
        models       = form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model=models)
        obj_id       = form.cleaned_data.get('object_id')
        texto_data   = form.cleaned_data.get('texto')

        comentarios,created = Comentarios.objects.get_or_create(

            usuario      = request.user,
            content_type = content_type,
            object_id    = obj_id,
            texto        = texto_data

        )

        return HttpResponseRedirect(comentarios.content_object.get_absolute_url())
        
        if created:
            print("Fue creado con exito")

    context = {

        'form'     :form,
        'instance' :instance

    }

    return render(request, 'comentario/comentar.html' , context)


