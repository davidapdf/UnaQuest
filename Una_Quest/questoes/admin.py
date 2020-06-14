from django.contrib import admin
from .models import Professor
from .models import Questao
from .models import Resposta
from users.models import Administrativo
from users.models import Disciplina
from users.models import Unidade

admin.site.register(Unidade)
admin.site.register(Professor)
admin.site.register(Administrativo)
admin.site.register(Disciplina)
admin.site.register(Resposta)
admin.site.register(Questao)
