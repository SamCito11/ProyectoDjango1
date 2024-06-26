from django.db import models

class Participante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
