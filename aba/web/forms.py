from django import forms
from django.forms import ModelForm
from web.models import Anuncio

class ContactoForm (forms.Form):
	nombre = forms.CharField(max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Tu nombre", 'id': "name", 'name': "name"}))
	email= forms.EmailField( 
		widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Tu email", 'id': "email", 'name': "email"}))
	mensaje = forms.CharField(
		widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Escribe aqui tu mensaje...", 'id': "message", 
			'name': "message", 'rows': "5"}))


class AnuncioForm(ModelForm):
	class Meta:
		model = Anuncio
		widgets = {
            'titulo': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Titulo anuncio", 'id': "titulo", 'name': "titulo"}),
        	'texto': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Escribe aqui el texto del anuncio...", 'id': "texto", 
			'name': "texto", 'rows': "5"}),
        }
        exclude = ['nick', 'fechaPublicacion']