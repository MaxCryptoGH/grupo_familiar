from django.db import models

class per_familia(models.Model):
    nombre = models.CharField(max_length=64)
    fechaNac = models.DateField()
    dni = models.IntegerField()
    