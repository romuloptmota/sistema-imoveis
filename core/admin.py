from django.contrib import admin

from .models import Edificio, Apartamento, Cliente

@admin.register(Edificio)
class Edificiodmin(admin.ModelAdmin):
    list_display = ('edificio',)


@admin.register(Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('edificio', 'apartamento', 'quartos', 'banheiros', 'vagas', 'tamanho', 'valor', 'codigo',
                    'disponivel', 'locatario', 'imagem1', 'imagem2', 'imagem3', 'imagem4', 'imagem5')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('locatario', 'email', 'telefone')
