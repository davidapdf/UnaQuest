from django.db import models

class Resposta(models.Model):
    descricao = models.CharField(max_length = 400)
    flegCerto = models.BooleanField(default=False)