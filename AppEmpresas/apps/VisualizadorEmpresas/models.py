from django.db import models
from datetime import datetime


# Create your models here.

class Empresa(models.Model):
    denominacion = models.CharField(max_length=128, verbose_name='Empresa, S.A', unique=True)
    telefono = models.CharField(max_length=50, verbose_name='111111111')
    horarioAtencion = models.CharField(max_length=256, verbose_name='Lunes-Viernes: 9:00 am a 18:00 pm')
    quienesSomos = models.CharField(max_length=1024, verbose_name='XXXXXXXXXXXXXXXXXXXXXXXXXXX')
    latitud = models.DecimalField(verbose_name='-32.89035681895765', max_digits=20, decimal_places=20)
    longitud = models.DecimalField(verbose_name=' -68.847745651633', max_digits=20, decimal_places=20)
    domicilio = models.CharField(max_length=256, verbose_name='San Martin 1580, Godoy Cruz, Mendoza')
    email = models.EmailField(verbose_name="empresa@empresa.com")

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']


class Noticia(models.Model):
    PUBLICADA_CHOICES = (
        ('Y', 'Y'),
        ('N', 'N'),
    )
    titulo = models.CharField(max_length=128, verbose_name='Título Noticia')
    resumen = models.CharField(max_length=1024, verbose_name='Resumen Noticia')
    imagen = models.ImageField(upload_to='imagenes/imagenesNoticias/%Y/%m/%d/')
    contenidoHTML = models.CharField(max_length=20480, verbose_name='Contenido HTML')
    publicada = models.CharField(max_length=1, help_text='Selecione Y si fue publicada, contrario seleccione N',
                                 choices=PUBLICADA_CHOICES)
    fechaPublicacion = models.DateField(auto_now=True, verbose_name='5/05/2021')
    fechaModificacion = models.DateField(auto_now_add=True, verbose_name='5/5/2021')

    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fechaPublicacion']
