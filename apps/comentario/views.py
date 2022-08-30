from django.shortcuts import render
from .models import Comentarios
from .forms import  ComentarioForm
from django.views.generic import DeleteView
from apps.usuario.models import Usuario
from django.urls import reverse_lazy




"""class AddComentario(DetailView):
    model = Comentarios
    template_name= "noticia/addcomentario.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = Comentarios.objects.all()
        return context"""


def AddComentario(request):
	usuario= Usuario(usuario=request.user)
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	
	
	context={
		'form': form,
		'usuario': usuario,
	}
	return render(request,'comentario/addcomentario.html', context)

class DeleteComentario(DeleteView):
	model 		  = Comentarios
	template_name = 'comentario/comentario_delete.html'
	success_url   = reverse_lazy('apps.noticia:listarNoticia2')

def Comentarioss(request):
	comentarios = Comentarios.objects.all()
	usuario = request.user.id

	context={
		'comentarios' : comentarios,
		'usuario': usuario,
	}
	return render(request,'comentario/listarcomentario.html', context)

