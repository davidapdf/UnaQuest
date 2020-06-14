from django.db import models
from datetime import datetime
from users.models import Professor

class Resposta(models.Model):
    descricao = models.TextField()
    flegCerto = models.BooleanField(default=False)

class Questao(models.Model):
    resposta = models.ForeignKey(Resposta, on_delete=models.CASCADE)
    user = models.OneToOneField(Professor, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateTimeField(default=datetime.now, blank=True)
    aprovado = models.BooleanField(default=False)
    
