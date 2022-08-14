from django.shortcuts import render
from .models import Comentarios
from .forms import  ComentarioForm
from apps.noticia.models import Noticia


def AddComentario(request):
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addcomentario.html', context)

def Comentarios(request):
	return render(request,'comentario/listarcomentario.html')