from django.contrib import admin

from sistema import models

# Aqui fica o registro do Usuário 
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'email', 'ativo',)

@admin.register(models.Genero)
class Genero(admin.ModelAdmin):
    list_display= ('id', 'nome')

@admin.register(models.filme)
class filme(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano','estudio','genero')

