from multiprocessing import context
from sre_constants import CATEGORY_UNI_LINEBREAK
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Noticia, Categoria 
from django.views.generic.detail import DetailView


class AddNoticia(CreateView):
    model         = Noticia
    fields        = ['titulo', 'subtitulo','texto','categoria','status','imagen']
    template_name = 'noticia/addNoticia.html'
    success_url   = reverse_lazy('index')

class ModificarNoticia(UpdateView):
	model 		  = Noticia
	form_class    = AddNoticia
	template_name = 'usuario/modificarNoticia.html'
	success_url   = reverse_lazy('index')

class PostDetailView(DetailView):
    model = Noticia
    template_name = 'noticia/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Noticia.objects.filter(slug=self.kwargs.get('slug'))
        return context

class DeleteNoticia(DeleteView):
	model 		  = Noticia
	template_name = 'noticia/noticia_confirm_delete.html'
	success_url   = reverse_lazy('index')

def ListarNoticia(request):
    noticia = Noticia.objects.all()
    categoria = Categoria.objects.all()
    
    context = {
        'noticia':noticia,
        'categoria': categoria,
    }
    return render(request,'noticia/listarNoticia2.html',context)

def ListarNoticiaPorCategoria(request,categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia    = Noticia.objects.filter(categoria=categoria2[0].id)
    context    = {
        'noticia' : noticia
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