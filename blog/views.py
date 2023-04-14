from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):
	posts = Post.objects.all()
	categorias = Categoria.objects.all().order_by('nombre')
	ctx = {'posts':posts, 'categorias':categorias}
	return render(request, 'blog/blog.html', ctx)

def categoria(request, categoria_id):
	categoria = Categoria.objects.get(id=categoria_id)
	posts = Post.objects.filter(categorias=categoria)
	return render(request, 'blog/categoria.html', {"categoria":categoria, "posts":posts})
