from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from carro.carro import Carro
from django.contrib.auth.models import User
from pedidos.models import LineaPedido, Pedidos
from tienda.models import Producto
from datetime import datetime

# Create your views here.

@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
	usuario = User.objects.all().filter(username=request.user)
	pedido = Pedidos.objects.create(user=request.user)
	carro = Carro(request)
	lineas_pedido = list()
	for key, value in carro.carro.items():
		lineas_pedido.append([key, value])
		producto = Producto.objects.all().filter(id = value['producto_id'])
		lp = LineaPedido()
		lp.user = usuario[0]
		lp.producto = producto[0]
		lp.pedido = pedido
		lp.cantidad = value['cantidad']
		lp.created_at = datetime.now()
		linea_pedido = lp.save()

	enviar_mail(pedido = pedido, 
		lineas_pedido = lineas_pedido, 
		nombreusuario = request.user.username,
		emailusuario = request.user.email)

	carro.limpiar_carro()
	messages.success(request, 'EL pedido se ha creado correctamente')
	return redirect('../tienda')

def enviar_mail(**kwargs):
	asunto = 'Gracias por el pedido'
	mensaje = render_to_string('tienda/emails/pedido.html', 
		{'pedido':kwargs.get('pedido'),
		'lineas_pedido': kwargs.get('lineas_pedido'),
		'nombreusuario': kwargs.get('nombreusuario')})
	mensaje_texto = strip_tags(mensaje)
	from_email = 'enrique_richard@hotmail.com'
	to = kwargs.get('emailusuario')
	send_mail(asunto, '', from_email, [str(to)], html_message = mensaje)
	return redirect('../tienda')
