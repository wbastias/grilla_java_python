from django.db import models
from django.utils import timezone

from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    rubro = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Trabajador(models.Model):
    nombre = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='trabajadores')

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    tipo = models.CharField(max_length=255)
    fecha = models.DateField(default=timezone.now)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='documentos')

    def __str__(self):
        return self.tipo
    


