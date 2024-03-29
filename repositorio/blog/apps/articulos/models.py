from django.db import models
from apps.usuarios.models import Usuario
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField

# Importar pytz para manejar timezones
import pytz


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.ImageField(upload_to='iconos/', default='iconos/default_icon.png')

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    # Cadena de texto en ForeignKey

    def __str__(self):
        return f"Comentario por {self.autor.username} en {self.fecha_creacion}"


class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    resumen = models.CharField(max_length=100, null=True)
    contenido = RichTextField(blank=True, null=True)
    # contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to = 'articulos', default='iconos/default_icon.png')
    categoria_articulo = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    # Para una BD nueva se debe crear sin default, sino provoca error al migrar
    # autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=Usuario.objects.filter(is_superuser=True).first().pk) 
    comentarios = models.ManyToManyField(Comentario, related_name='articulo')

    def __str__(self):
        return self.titulo

