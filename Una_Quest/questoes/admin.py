from django.contrib import admin
from .models import Professor
from .models import Questao
from users.models import Administrativo
from users.models import Disciplina
from users.models import Unidade
from provas.models import Prova,ProvaAdmin
from django.forms import CheckboxSelectMultiple


admin.site.register(Prova, ProvaAdmin)
admin.site.register(Questao)
admin.site.register(Unidade)
admin.site.register(Professor)
admin.site.register(Administrativo)
admin.site.register(Disciplina)