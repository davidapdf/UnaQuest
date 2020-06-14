from django.db import models
from datetime import datetime
from users.models import Professor

class Resposta(models.Model):
    descricao = models.CharField(max_length = 400)
    flegCerto = models.BooleanField(default=False)

class Questao(models.Model):
    resposta = models.ManyToManyField(Resposta)
    user = models.ForeignKey(Professor, on_delete=models.CASCADE)
    descricao = models.CharField(max_length = 5000)
    data = models.DateTimeField(default=datetime.now, blank=True)
    aprovado = models.BooleanField(default=False)
    
