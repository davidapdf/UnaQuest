from django.db import models
from datetime import datetime
from users.models import Professor
from multiselectfield import MultiSelectField


MY_CHOICES2 = ((1, 'Questão 1'),
               (2, 'Questão 2'),
               (3, 'Questão 3'),
               (4, 'Questão 4'),
               (5, 'Questão 5'))


class Questao(models.Model):
    user = models.ForeignKey(Professor, on_delete=models.CASCADE)
    descricao = models.TextField(default='NA')
    data = models.DateTimeField(default=datetime.now, blank=True)
    resposta1 = models.TextField(default='NA')
    resposta2 = models.TextField(default='NA')
    resposta4 = models.TextField(default='NA')
    resposta5 = models.TextField(default='NA')
    resposta_correta = MultiSelectField(choices=MY_CHOICES2,
                                 max_choices=1,
                                 max_length=1)
    aprovado = models.BooleanField(default=False)
