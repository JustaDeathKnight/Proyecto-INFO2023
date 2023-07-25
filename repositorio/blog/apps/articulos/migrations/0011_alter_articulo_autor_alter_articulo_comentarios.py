<<<<<<< HEAD
# Generated by Django 4.2.3 on 2023-07-25 21:53
=======
# Generated by Django 4.2.3 on 2023-07-25 20:19
>>>>>>> 7371b795c44399c01e6b0e09de00afb0308af29e

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articulos', '0010_remove_articulo_comentarios_articulo_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='comentarios',
            field=models.ManyToManyField(related_name='articulo', to='articulos.comentario'),
        ),
    ]
