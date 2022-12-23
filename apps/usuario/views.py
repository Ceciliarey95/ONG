from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Usuario
from .forms import RegistroUsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin

class RegistrarUsuario(CreateView):
	model         = Usuario
	form_class    = RegistroUsuarioForm
	template_name = 'usuario/registrar.html'
	success_url   = reverse_lazy('apps.usuario:login')

def ListarUsuario(request):
    usuario    = Usuario.objects.all()
    context = {
        'usuario':usuario,
    }
    return render(request,'base.html',context)

def Usuarios(request):
	usuarios = Usuario.objects.all()
	context={
		'usuarios': usuarios,
	}
	return render(request,'usuario/listarUsuarios.html', context)

class UpdateUsuario(LoginRequiredMixin,UpdateView):
    model         = Usuario
    fields        = ['username','first_name','last_name','email','imagen']
    template_name = 'usuario/registrar.html'
    success_url   = reverse_lazy('index')

class DeleteUsuario(DeleteView):
	model 		  = Usuario
	template_name = 'usuario/usuario_delete.html'
	success_url   = reverse_lazy('apps.usuario:listarUsuarios')
