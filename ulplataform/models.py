from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User

# Create your models here.

class Uplink(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    uplink_name = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=40)
    foto = models.ImageField( upload_to='img/', height_field=None, width_field=None, max_length=None)
    links = models.JSONField(default=list)
    links_redes = models.JSONField(default=list)
    tema = models.CharField(max_length=20, default='default-theme')


class UplinkTheme(models.Model):
    nome_tema = models.CharField(max_length=20)
    estilo = models.CharField(max_length=1000)