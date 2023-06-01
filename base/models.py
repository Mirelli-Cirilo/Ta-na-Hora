from django.db import models

class Remedio(models.Model):
    nome = models.CharField(max_length=70)
    horario = models.TimeField(default='16:00:00')
    descricao = models.TextField()

    def __str__(self):
        return self.nome
