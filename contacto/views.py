from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
	formulario_contacto = FormularioContacto()

	if (request.method == 'POST'):
		formulario_contacto = FormularioContacto(data=request.POST)
		if (formulario_contacto.is_valid()):
			asunto = 'Gracias por contactarnos'
			nombre = request.POST.get("nombre")
			from_email = 'enrique_richard@hotmail.com'
			to = request.POST.get("email")
			contenido = request.POST.get("contenido")
			# mensaje = 'Sr. ' + nombre + 'Su consulta ' +  contenido
			mensaje = render_to_string('contacto/email.html', 
					{'nombre':nombre,
					'contenido': contenido}
			)
			try:
				send_mail(asunto, '', from_email, [to], html_message = mensaje)
				return redirect('/contacto')
			except:
				return redirect('/contacto')

	return render(request, 'contacto/contacto.html', {"miFormulario":formulario_contacto})
