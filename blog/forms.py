from django import forms
from django.contrib.auth.models import User
from .models import Categoria

class NewblogForm(forms.Form):
    titulo = forms.CharField(label='Titulo', max_length=50)
    contenido = forms.CharField(label='contenido', max_length=50)
    imagen = forms.ImageField(label='imagen', max_length=50)
    autor = forms.ModelChoiceField(label='autor', queryset=User.objects.all())
    categorias = forms.ModelChoiceField(label='Categoria', queryset=Categoria.objects.all())

#color = forms.ModelChoiceField(queryset=Color.objects.all())
	# titulo = models.CharField(max_length=50)
	# contenido = models.CharField(max_length=50)
	# imagen = models.ImageField(upload_to='blog', null=True, blank=True)
	# autor = models.ForeignKey(User, on_delete=models.CASCADE)
	# categorias = models.ManyToManyField(Categoria)
	# created = models.DateTimeField(auto_now_add=True)
	# updated = models.DateTimeField(auto_now_add=True)
