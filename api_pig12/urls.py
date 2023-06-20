from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_pig12 import views

router = DefaultRouter()
router.register(r'post', views.PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]