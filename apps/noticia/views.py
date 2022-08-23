from multiprocessing import context
from sre_constants import CATEGORY_UNI_LINEBREAK
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Noticia, Categoria 
from apps.comentario.models import Comentarios
from apps.usuario.models import Usuario
from apps.comentario.forms import ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin



class AddNoticia(LoginRequiredMixin, CreateView):
    model         = Noticia
    fields        = ['titulo', 'subtitulo','texto','categoria','imagen']
    template_name = 'noticia/addNoticia.html'
    success_url   = reverse_lazy('index')


class AddCategoria(LoginRequiredMixin,CreateView):
    model         = Categoria
    fields        = ['nombre', 'id']
    template_name = 'noticia/addCategoria.html'
    success_url   = reverse_lazy('index')


class UpdateNoticia(LoginRequiredMixin,UpdateView):
    model         = Noticia
    fields        = ['titulo', 'subtitulo','texto','categoria','imagen']
    template_name = 'noticia/addNoticia.html'
    success_url   = reverse_lazy('index')


class DeleteNoticia(LoginRequiredMixin,DeleteView):
	model 		  = Noticia
	template_name = 'noticia/noticia_confirm_delete.html'
	success_url   = reverse_lazy('index')


def ListarNoticia(request):
    noticia    = Noticia.objects.all()
    categoria  = Categoria.objects.all()
    
    context = {
        'noticia':noticia,
        'categoria': categoria,
    }
    return render(request,'noticia/listarNoticia2.html',context)

def ListarNoticiaPorCategoria(request,categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia    = Noticia.objects.filter(categoria=categoria2[0].id)
    categorias  = Categoria.objects.all()
    context    = {
        'noticia' : noticia,
        'categoria':categorias
    }
    return render(request,'noticia/listarPorCategoria.html',context)

def noticias(request):
    noticias = Noticia.objects.get(all)
    return render(noticias)

def ExistePost(id):
    for i in noticias:
        if i.id == id:
            return i
    return None

def ReadPost(request, id):
	try:
		posts   = ExistePost(id)
	except Exception:
		posts   = Noticia.objects.get(id=id)
	comentarios = Comentarios.objects.filter(noticia=id)

	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		if request.user.is_authenticated:
			aux         =  form.save(commit=False)
			aux.noticia = posts
			aux.user    = request.user
			aux.save()
			form        = ComentarioForm()
		else:
			return redirect('usuario:login')
	context = {
		'titulo': 'noticia',
		'posts': posts,
		'form': form,
		'comentarios': comentarios,
	}
	return render(request,'noticia/post.html', context)

"""def darLike(request, pk):
    noticia = get_object_or_404(Noticia, id=pk)
    if request.user in noticia.likes.all():
        noticia.likes.remove(request.user)
    else:
        noticia.likes.add(request.user.id)
    return redirect('/noticia/'+str(noticia.id))
"""
