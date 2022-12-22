from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .models import Usuario
from .forms import RegistroUsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin

class RegistrarUsuario(CreateView):
	model         = Usuario
	form_class    = RegistroUsuarioForm
	template_name = 'usuario/registrar.html'
	success_url   = reverse_lazy('apps.usuario:login')

def ListarUsuario(LoginRequiredMixin,request):
    usuario    = Usuario.objects.all()
    context = {
        'usuario':usuario,
    }
    return render(request,'base.html',context)

<<<<<<< HEAD
def Usuarios(request):
	usuarios = Usuario.objects.all()
	context={
		'usuarios': usuarios,
	}
	return render(request,'usuario/listarUsuarios.html', context)

class DeleteUsuario(DeleteView):
	model 		  = Usuario
	template_name = 'usuario/usuario_delete.html'
	success_url   = reverse_lazy('apps.usuario:listarUsuarios')
=======
>>>>>>> c9db5b9352f281ad2b8045e219e87800e1eb3397
