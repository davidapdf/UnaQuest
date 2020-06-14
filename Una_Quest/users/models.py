from django.db import models
from django.contrib.auth.models import User


class Unidade(models.Model):
    cidade = models.TextField()
    descricao = models.TextField()
    estado = models.TextField()

class Disciplina(models.Model):
    nome = models.TextField()
    descricao = models.CharField(max_length=500,blank=True,null=True)

class Professor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    diciplina = models.ManyToManyField(Disciplina)
    unidade = models.OneToOneField(Unidade, on_delete=models.CASCADE)
    

class Administrativo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    unidade = models.OneToOneField(Unidade, on_delete=models.CASCADE)