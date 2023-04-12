from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pedidos.models import LineaPedido, Pedidos
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# from django.core.mail import send_mail
from carro.carro import Carro

# Create your views here.

@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido = Pedidos.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value['cantidad'],
            user = request.user,
            pedido = pedido))
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(pedido = pedido, 
        lineas_pedido = lineas_pedido, 
        nombreusuario = request.user.username,
        emailusuario = request.user.email)

    messages.success(request, 'EL pedido se ha creado correctamente')
    return redirect('../tienda')

def enviar_mail(**kwargs):
    asunto = 'Gracias por el pedido'
    mensaje = render_to_string('tienda/emails/pedido.html', 
        {'pedido':kwargs.get('pedido'),
        'lineas_pedido': kwargs.get('lineas_pedido'),
        'nombreusuario': kwargs.get('nombreusuario')})
    mensaje_texto = strip_tags(mensaje)
    from_email = 'enrique.richard@gmail.com'
    to = kwargs.get('emailusuario')
    # send_mail(asunto, mensaje_texto, from_email, [to], html_message = mensaje)
    return redirect('../tienda')
