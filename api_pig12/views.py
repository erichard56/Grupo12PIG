from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Post
from api_pig12 import serializers

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('autor', 'titulo')
	serializer_class = serializers.PostSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

