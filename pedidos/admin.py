from django.contrib import admin
from .models import Pedidos, LineaPedido

# Register your models here.

admin.site.register([Pedidos, LineaPedido])
