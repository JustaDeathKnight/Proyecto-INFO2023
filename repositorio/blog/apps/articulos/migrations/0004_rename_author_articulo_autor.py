# Generated by Django 4.2.3 on 2023-07-22 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0003_articulo_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='author',
            new_name='autor',
        ),
    ]
