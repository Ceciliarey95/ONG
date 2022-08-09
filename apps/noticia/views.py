from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Noticia, Categoria 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse

class AddNoticia(CreateView):
    model         = Noticia
    fields        = ['titulo','texto','categoria','imagen']
    template_name = 'noticia/addNoticia.html'
    success_url   = reverse_lazy('index')

class MostrarNoticia(ListView):
    model         = Noticia
    template_name = 'noticia/listarNoticia.html'

    """def get_queryset(self):
        ------------------------"""

def ListarNoticia(request):
    noticia = Noticia.objects.all()
    context = {
        'noticia':noticia
    }
    return render(request,'noticia/listarNoticia2.html',context)

def ListarNoticiaPorCategoria(request,categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia    = Noticia.objects.filter(categoria=categoria2[0].id)
    context    = {
        'noticia' : noticia,
    }
    return render(request,'noticia/listarNoticia2.html',context)


"""class AddLike(LoginRequiredMixin, View):
    def noticia(self, request, pk,*args,**kwargs):
        noticia = Noticia.objects.get(pk=pk)

        is_dislike         = False
        for dislike in noticia.dislikes.all():
            if dislike     == request.user:
                is_dislike = True
                break

        if is_dislike:
            noticia.dislikes.remove(request.user)

        is_like         = False
        for like in noticia.likes.all():
            if like     == request.user:
                is_like = True
                break

        if not is_like:
            noticia.likes.add(request.user)

        if is_like:
            noticia.likes.remove(request.user)

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def noticia(self, request, pk,*args,**kwargs):
        noticia = Noticia.objects.get(pk=pk)

        is_like = False
        for like in noticia.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            noticia.likes.remove(request.user)

        is_dislike = False
        for dislike in noticia.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            noticia.dislikes.add(request.user)

        if is_dislike:
            noticia.dislikes.remove(request.user)

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)"""