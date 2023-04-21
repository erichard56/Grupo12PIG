from django import forms
from django.contrib.auth.models import User
from .models import Categoria

class NewblogForm(forms.Form):
    titulo = forms.CharField(label='Titulo', max_length=50)
    contenido = forms.CharField(max_length=500, 
        			widget=forms.Textarea(
        				attrs={'name':'Contenido'})
				)
    imagen = forms.ImageField(label='Imagen', max_length=50)
    autor = forms.ModelChoiceField(label='Autor', queryset=User.objects.all())
    categorias = forms.ModelChoiceField(label='Categoria', queryset=Categoria.objects.all())
