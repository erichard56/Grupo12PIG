from rest_framework import serializers
from blog.models import Post, Categoria
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    
	class Meta:
		model = Post
		fields = ['id', 'titulo', 'contenido', 'created', ]
