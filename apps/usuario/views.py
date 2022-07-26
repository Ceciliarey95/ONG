from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Usuario
from .forms import RegistroUsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin

""" from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = Usuario
		#fields = UserCreationForm.Meta.fields + ('imagen')
		template_name = 'usuario/registrar.html' """

class RegistrarUsuario(CreateView):
	model         = Usuario
	form_class    = RegistroUsuarioForm
	template_name = 'usuario/registrar.html'
	success_url   = reverse_lazy('index')

def ListarUsuario(LoginRequiredMixin,request):
    usuario    = Usuario.objects.all()
    context = {
        'usuario':usuario,
    }
    return render(request,'base.html',context)

