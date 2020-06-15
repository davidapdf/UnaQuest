from django.db import models
from questoes.models import Questao
from users.models import Professor
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
#from multiselectfield import MultiSelectField



class Prova(models.Model):
    descricao = models.CharField(max_length=500,blank=False,null=False)
    nome_prova = models.TextField(default='NA')
    questoes = models.ManyToManyField(Questao)
    usuario = models.ForeignKey(Professor, on_delete=models.CASCADE) 


class ProvaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = ('id','nome_prova','Professor')
    def Professor(self,Prova):
        return Prova.usuario.user