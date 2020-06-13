from django.db import models
from questoes.models import Questao
from django.contrib.auth.models import User

class Prova(models.Model):
    questoes = models.ManyToManyField(Questao)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)