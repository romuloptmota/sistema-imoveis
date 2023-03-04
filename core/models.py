from django.db import models

from stdimage.models import StdImageField


class Edificio(models.Model):
    edificio = models.CharField('Edifício', max_length=100)

    def __str__(self):
        return self.edificio


class Apartamento(models.Model):
    edificio = models.ForeignKey("Edificio", on_delete=models.PROTECT)
    apartamento = models.DecimalField('Nº Apto', decimal_places=0, max_digits=10)
    quartos = models.DecimalField('Nº de quartos', decimal_places=0, max_digits=2)
    banheiros = models.DecimalField('Nº de banheiros', decimal_places=0, max_digits=2)
    vagas = models.DecimalField('Nº de vagas', decimal_places=0, max_digits=2)
    tamanho = models.DecimalField('m²', decimal_places=0, max_digits=4)
    codigo = models.DecimalField('cod. identificação', decimal_places=0, max_digits=10, unique=True)
    valor = models.DecimalField('Valor', decimal_places=0, max_digits=10)
    imagem1 = StdImageField('Imagem 1', upload_to='apartamentos', variations={'thump': {'width': 457, 'height': 367, 'crop': True}})
    imagem2 = StdImageField('Imagem 2', upload_to='apartamentos', variations={'thump': {'width': 457, 'height': 367, 'crop': True}})
    imagem3 = StdImageField('Imagem 3', upload_to='apartamentos', variations={'thump': {'width': 457, 'height': 367, 'crop': True}})
    imagem4 = StdImageField('Imagem 4', upload_to='apartamentos', variations={'thump': {'width': 457, 'height': 367, 'crop': True}})
    imagem5 = StdImageField('Imagem 5', upload_to='apartamentos', variations={'thump': {'width': 457, 'height': 367, 'crop': True}})
    disponivel = models.BooleanField('Disponivel?', default=True)
    locatario = models.OneToOneField("Cliente", on_delete=models.PROTECT, blank=True, null=True)


class Cliente(models.Model):
    locatario = models.CharField('Locatario', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)

    def __str__(self):
        return self.locatario
