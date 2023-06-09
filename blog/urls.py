from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	path('', views.blog, name='Blog'),
	path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
	path('newpost/', views.newpost, name='newpost'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
