from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

# class CategoriaAdmin(admin.ModelAdmin):
# 	readonly_fields = ('created', 'updated')

# class PostAdmin(admin.ModelAdmin):
# 	readonly_fields = ('created', 'updated')

# admin.site.register(Categoria, CategoriaAdmin)
# admin.site.register(Post, PostAdmin)

class CategoriaInline(admin.TabularInline):
	model = Post.categorias.through

class CategoriaAdmin(admin.ModelAdmin):
	inlines = [
		CategoriaInline
	]

class PostAdmin(admin.ModelAdmin):
	inlines = [
		CategoriaInline
	]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)