from django.db import models
from django.contrib.auth.models import User

class Remedio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=70)
    horario = models.TimeField(default='16:00')
    descricao = models.TextField()

    def __str__(self):
        return self.nome
