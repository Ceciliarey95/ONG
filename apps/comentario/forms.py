from django import forms
from .models import Comentarios

class ComentarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['texto'].widget.attrs.update({'rows': '3'})

    class Meta:
        model = Comentarios
        fields = ['texto']
        exclude = ['noticia']

"""class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':'2', 
            'placeholder':'Escribe un comentario...',
            }), required=True, max_length=250, label='Comentario')
    class Meta:
        model = Comentarios
        fields = ('texto',)"""