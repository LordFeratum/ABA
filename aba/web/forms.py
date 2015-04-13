from django import forms
from django.forms import ModelForm
from web.models import Anuncio
from datetime import datetime

class ContactoForm (forms.Form):
	nombre = forms.CharField(max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Tu nombre", 'id': "name", 'name': "name"}))
	email= forms.EmailField( 
		widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Tu email", 'id': "email", 'name': "email"}))
	mensaje = forms.CharField(
		widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Escribe aqui tu mensaje...", 'id': "message", 
			'name': "message", 'rows': "5"}))


class AnuncioForm(ModelForm):
	
	def __init__(self, user, *args, **kwargs):
		super(AnuncioForm, self).__init__(*args, **kwargs)
		self.user = user


	class Meta:
		model = Anuncio
		fields = ('titulo', 'texto', 'imagen')
		widgets = {
            'titulo': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Titulo anuncio", 'id': "titulo", 'name': "titulo"}),
        	'texto': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Escribe aqui el texto del anuncio...", 'id': "texto", 
			'name': "texto", 'rows': "5"}),
        }


	def save(self, force_insert=False, force_update=False, commit=True):
		m = super(AnuncioForm, self).save(commit=False)
		m.nick = self.user
		m.fechaPublicacion = datetime.now()
		if commit:
			m.save()
			return m
		