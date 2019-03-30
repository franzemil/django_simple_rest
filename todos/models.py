from django.contrib.auth.models import User
from django.db import models


class Tarea(models.Model):
    nombre = models.CharField(max_length=140)
    terminado = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='taks', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
