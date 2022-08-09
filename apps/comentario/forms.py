from django import forms

class FormComentarios(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id    = forms.IntegerField(widget=forms.HiddenInput)
    texto        = forms.CharField(widget=forms.Textarea)