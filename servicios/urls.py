from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.servicios, name='Servicios'),
    path('servicio_borrar/<int:id>', views.servicio_borrar, name='servicio_borrar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
