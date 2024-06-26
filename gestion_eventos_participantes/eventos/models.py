from django.db import models
from participantes.models import Participante

class Evento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=200)
    participantes = models.ManyToManyField(Participante, through='Asistencia')

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.participante} en {self.evento}'
