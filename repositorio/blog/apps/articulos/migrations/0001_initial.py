# Generated by Django 4.2.3 on 2023-08-03 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                (
                    "icono",
                    models.ImageField(
                        default="iconos/default_icon.png", upload_to="iconos/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comentario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contenido", models.TextField()),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_modificacion", models.DateTimeField(auto_now=True)),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Articulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("resumen", models.CharField(max_length=100, null=True)),
                ("contenido", models.TextField()),
                ("fecha_publicacion", models.DateTimeField(auto_now_add=True)),
                (
                    "imagen",
                    models.ImageField(
                        default="iconos/default_icon.png", upload_to="articulos"
                    ),
                ),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "categoria_articulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articulos.categoria",
                    ),
                ),
                (
                    "comentarios",
                    models.ManyToManyField(
                        related_name="articulo", to="articulos.comentario"
                    ),
                ),
            ],
        ),
    ]
