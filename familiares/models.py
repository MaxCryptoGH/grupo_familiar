from django.db import models

class per_familia(models.Model):
    nombre = models.CharField(max_lenght=64)
    fechaNac = models.DateField()
    dni = models.IntegerField()
    pass