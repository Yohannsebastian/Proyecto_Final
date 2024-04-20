from django.db import models

# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre',null=False)
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    correo = models.EmailField(verbose_name='Correo electronico')
    mensaje = models.CharField(max_length=500, verbose_name='Mensaje')
    