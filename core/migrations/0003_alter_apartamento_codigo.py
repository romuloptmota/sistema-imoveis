# Generated by Django 4.1.7 on 2023-03-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_apartamento_cliente_rename_building_edificio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartamento',
            name='codigo',
            field=models.DecimalField(decimal_places=0, max_digits=10, unique=True, verbose_name='cod. identificação'),
        ),
    ]