from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import CheckboxSelectMultiple


class Unidade(models.Model):
    cidade = models.CharField(max_length = 200)
    estado = models.CharField(max_length = 2)
    descricao = models.TextField()
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=500,blank=False,null=False)
    descricao = models.TextField()

class Professor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    diciplina = models.ManyToManyField(Disciplina)
    unidade = models.OneToOneField(Unidade, on_delete=models.CASCADE)
    def __ini__(self,user,diciplina,unidade):
        self.user = user
        self.diciplina = diciplina
        self.unidade = unidade


class ProfessorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = ('id','user','unidade')
    
class Administrativo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    unidade = models.OneToOneField(Unidade, on_delete=models.CASCADE)

