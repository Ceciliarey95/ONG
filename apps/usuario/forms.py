#from django.contrib.auth.models import User
from .models import Usuario
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm


class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model  = Usuario
        fields = ['first_name','last_name','username','password1','password2','email', 'imagen']

    @transaction.atomic
    def save(self):
        user              = super().save(commit=False)
        user.is_superuser = False
        user.is_staff     = False
        user.save()
        return user
