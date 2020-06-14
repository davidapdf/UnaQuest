from django.db import models
from questoes.models import Questao
from users.models import Professor

class Prova(models.Model):
    descricao = models.CharField(max_length = 5000)
    nome_prova = models.TextField()
    questoes = models.ManyToManyField(Questao)
    usuario = models.ForeignKey(Professor, on_delete=models.CASCADE) 
    