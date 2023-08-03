# Generated by Django 4.2.3 on 2023-07-24 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0009_articulo_comentarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='comentarios',
        ),
        migrations.AddField(
            model_name='articulo',
            name='comentarios',
            field=models.ManyToManyField(blank=True, related_name='articulo', to='articulos.comentario'),
        ),
    ]