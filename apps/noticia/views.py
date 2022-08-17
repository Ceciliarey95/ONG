from multiprocessing import context
from sre_constants import CATEGORY_UNI_LINEBREAK
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Noticia, Categoria 
from apps.comentario.models import Comentarios
from apps.comentario.forms import ComentarioForm


class AddNoticia(CreateView):
    model         = Noticia
    fields        = ['titulo', 'subtitulo','texto','categoria','imagen']
    template_name = 'noticia/addNoticia.html'

class AddCategoria(CreateView):
    model         = Categoria
    fields        = ['nombre', 'id']
    template_name = 'noticia/addCategoria.html'
    success_url   = reverse_lazy('index')

class ModificarNoticia(UpdateView):
    noticia       = Noticia
    fields        =  ['titulo', 'subtitulo','texto','categoria','imagen']
    template_name = 'noticia/modificarNoticia.html' 

class DeleteNoticia(DeleteView):
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

def botonCategoria(request):
    categorias = Categoria.objects.filter()

def ListarNoticiaPorCategoria(request,categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia    = Noticia.objects.filter(categoria=categoria2[0].id)
    context    = {
        'noticia' : noticia
    }
    return render(request,'noticia/listarPorCategoria.html',context)


def ListarNoticiaPorFecha(request,fecha):
    noticia    = Noticia.objects.filter(fecha=fecha)
    context    = {
        'noticia' : noticia
    }
    return render(request,'noticia/listarPorFecha.html',context)

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
			aux =  form.save(commit=False)
			aux.noticia = posts
			aux.user = request.user
			aux.save()
			form = ComentarioForm()
		else:
			return redirect('usuario:login')
	
	context = {
		'titulo': 'post',
		'posts': posts,
		'form': form,
		'comentarios': comentarios,
	}
	return render(request,'noticia/post.html', context)
