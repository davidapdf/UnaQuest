from django.db import models
from datetime import datetime
from users.models import Professor

class Questao(models.Model):
    user = models.ForeignKey(Professor, on_delete=models.CASCADE)
    descricao = models.TextField(default='NA')
    data = models.DateTimeField(default=datetime.now, blank=True)
    resposta1 = models.TextField(default='NA')
    resposta2 = models.TextField(default='NA')
    resposta4 = models.TextField(default='NA')
    resposta5 = models.TextField(default='NA')
    resposta_correta = models.SmallIntegerField()
    aprovado = models.BooleanField(default=False)

 







    
