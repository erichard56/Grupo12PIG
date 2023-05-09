from django.urls import path
from .views import VRegistro, cerrar_sesion, logear, act_des, activa

urlpatterns = [
	path('', VRegistro.as_view(), name='Autenticacion'),
	path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
	path('logear', logear, name='logear'),
	path('act_des', act_des, name='act_des'),
	path('activa/<str:fnc>/<int:id>', activa, name='activa'),
]

