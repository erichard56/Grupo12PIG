from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

# Create your models here.

User = get_user_model()

class Pedidos(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add = True)

	def __str__(self):
		return f'{str(self.id)} / {self.user}'

	class Meta:
		db_table = 'pedidos'
		verbose_name = 'pedido'
		verbose_name_plural = 'pedidos'
		ordering = ['id']

class LineaPedido(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default = 1)
	created_at = models.DateField(auto_now_add = True)

	def __str__(self):
		return(f'{self.cantidad} unidades de {self.producto}')

	class Meta:
		db_table = 'lineapedidos'
		verbose_name = 'Linea Pedido'
		verbose_name_plural = 'Lineas Pedidos'
		ordering = ['id']
