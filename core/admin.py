from django.contrib import admin

from .models import Building, Apartament, Client


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('edificio',)


@admin.register(Apartament)
class ApartamentAdmin(admin.ModelAdmin):
    list_display = ('edificio', 'apartamento', 'quartos', 'banheiros', 'vagas', 'tamanho', 'valor',
                    'imagem1', 'imagem2', 'imagem3', 'imagem4', 'imagem5', 'disponivel', 'locatario')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'email', 'telefone')
