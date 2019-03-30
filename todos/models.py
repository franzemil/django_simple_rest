from django.db import models


class Tarea(models.Model):
    nombre = models.CharField(max_length=140)
    terminado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
