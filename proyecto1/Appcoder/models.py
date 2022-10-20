from django.db import models

# Create your models here.

class Falimiares(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()