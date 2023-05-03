from django.shortcuts import render, redirect
from django.views.generic import View
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.

class UserCreationFormWithEmail(UserCreationForm):
	email = forms.EmailField(required = True,
			  help_text = 'Requerido. 254 caracteres como máximo y debe ser un email válido')
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class VRegistro(View):

	def get(self, request):
		form = UserCreationFormWithEmail()
		return render(request, 'autenticacion/registro/registro.html', {'form':form})

	def post(self, request):
		form = UserCreationFormWithEmail(request.POST)
		if (form.is_valid()):
			eml = request.POST['email']
			user = User.objects.all().filter(email = eml)
			if (not user):
				usuario = form.save()
				login(request, usuario)
				return redirect('Home')
			else:
				messages.add_message(request, messages.WARNING, 'email ya utilizado')
	# else:
		for msg in form.error_messages:
			messages.error(request, form.error_messages[msg])
		return render(request, 'autenticacion/registro/registro.html', {'form':form})

def cerrar_sesion(request):
	logout(request)
	return redirect('Home')

def logear(request):
	if (request.method == 'POST'):
		form = AuthenticationForm(request, data=request.POST)
		existe_usuario = User.objects.filter(username = request.POST['username']).exists()
		if (existe_usuario):
			user = User.objects.all().filter(username = request.POST['username'])
			if(user[0].is_active):
				if (form.is_valid()):
					nombre_usuario = form.cleaned_data.get('username')
					contra = form.cleaned_data.get('password')
					usuario = authenticate(username = nombre_usuario, password = contra)
					if (usuario is not None):
						login(request, usuario)
						return redirect('Home')
					else:
						messages.error(request, 'usuario no valido')
				else:
					messages.error(request, 'Informacion incorrecta')
			else:
				messages.error(request, 'El usuario no esta activo. Avise al Administrador')
		else:
			messages.error(request, 'El usuario no existe')
	
	form = AuthenticationForm()
	return render(request, 'autenticacion/login/login.html', {'form':form})
