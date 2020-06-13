from django.db import models
from respostas.models import Resposta
from usuarios.models import Professor
from datetime import datetime


class Questao(models.Model):
    resposta = models.ManyToManyField(Resposta)
    user = models.ForeignKey(Professor, on_delete=models.CASCADE)
    descricao = models.CharField(max_length = 5000)
    data = models.DateTimeField(default=datetime.now, blank=True)
    aprovado = models.BooleanField(default=False)
    