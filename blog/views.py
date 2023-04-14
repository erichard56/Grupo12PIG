from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, Categoria
from .forms import NewblogForm
from django.contrib.auth.models import User

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

def newpost(request):
    if request.method == 'POST':
        userform = NewblogForm(request.POST, request.FILES)
        if userform.is_valid():
            titulo = userform.cleaned_data['titulo']
            contenido = userform.cleaned_data['contenido']
            imagen = userform.cleaned_data['imagen']

            _autor = userform.cleaned_data['autor']
            autor = User.objects.all().filter(username=_autor).first()
            
            _categorias = userform.cleaned_data['categorias']
            cate = Categoria.objects.all().filter(nombre=_categorias)

            #Guardar datos
            new_post = Post.objects.create(titulo=titulo, contenido=contenido, imagen = imagen, autor = autor)
            new_post.categorias.set(cate)
            new_post.save()
            return redirect('/blog')

    else:
        userform = NewblogForm()
    return render(request, 'blog/newpost.html',{'userform':userform})