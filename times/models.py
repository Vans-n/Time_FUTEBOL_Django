from django.db import models

class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    ano_fundacao = models.IntegerField()
    estadio = models.CharField(max_length=100)

    def __str__(self):
        return self.nome