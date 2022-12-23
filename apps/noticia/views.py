from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Noticia, Categoria, MeGusta
from apps.comentario.models import Comentarios
from apps.comentario.forms import ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class AddNoticia(LoginRequiredMixin, CreateView):
    model         = Noticia
    fields        = ['titulo', 'subtitulo','texto','categoria','imagen']
    template_name = 'noticia/addNoticia.html'
    success_url   = reverse_lazy('apps.noticia:listarNoticia2')


class AddCategoria(LoginRequiredMixin,CreateView):
    model         = Categoria
    fields        = ['nombre', 'id']
    template_name = 'noticia/addCategoria.html'
    success_url   = reverse_lazy('index')


class UpdateNoticia(LoginRequiredMixin,UpdateView):
    model         = Noticia
    fields        = ['titulo', 'subtitulo','texto','categoria','imagen']
    template_name = 'noticia/addNoticia.html'
    success_url   = reverse_lazy('apps.noticia:listarNoticia2')


class DeleteNoticia(LoginRequiredMixin,DeleteView):
	model 		  = Noticia
	template_name = 'noticia/noticia_confirm_delete.html'
	success_url   = reverse_lazy('apps.noticia:listarNoticia2')

class ListarNoticiasClase(ListView):
    template_name= "noticia/listarNoticia2.html"
    model = Noticia
    context_object_name = "noticias"
    paginate_by = 2

    def get_queryset(self):
        noticias = Noticia.objects.all()
        titulo_noticia = self.request.GET.get("Buscador")
        if titulo_noticia:
            noticias = noticias.filter(titulo__contains=titulo_noticia)

        return noticias.order_by("titulo")
   

def dar_me_gusta(request, id_noticia):
    mg = MeGusta.objects.filter(usuario=request.user, noticia__id=id_noticia)
    if not mg:
        mg = MeGusta.objects.create(usuario=request.user, noticia=Noticia.objects.get(id=id_noticia))
    return HttpResponseRedirect(reverse("apps.noticia:listarNoticia2"))




"""def ListarNoticia(request):
    noticia    = Noticia.objects.all()
    categoria  = Categoria.objects.all()
    template_name='noticia/listarNoticia2.html'
    context = {
        'noticia':noticia,
        'categoria': categoria,
    }
    return render(request,template_name,context)"""

def ListarNoticiaPorCategoria(request,categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia    = Noticia.objects.filter(categoria=categoria2[0].id)
    categorias  = Categoria.objects.all()
    template_name='noticia/listarPorCategoria.html'
    context    = {
        'noticia' : noticia,
        'categoria':categorias
    }
    return render(request,template_name,context)

def noticias(request):
    noticias = Noticia.objects.get(all)
    return render(request,noticias)

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
			aux.usuario = request.user
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