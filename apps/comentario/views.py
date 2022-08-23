from django.shortcuts import render
from .models import Comentarios
from .forms import  ComentarioForm
from apps.usuario.models import Usuario


def AddComentario(request):
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	
	context={
		'form': form,
	}
	return render(request,'comentario/addcomentario.html', context)

def Comentarioss(request):
	comentarios = Comentarios.objects.all()
	context={
		'comentarios' : comentarios,
	}
	return render(request,'comentario/listarcomentario.html', context)

