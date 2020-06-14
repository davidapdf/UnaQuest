from django.contrib import admin
from .models import Professor
from .models import Questao
from users.models import Administrativo
from users.models import Disciplina
from users.models import Unidade

class QuestaoAdmin(admin.ModelAdmin):
    model = Questao
    list_display = ['descricao','resposta_descricao']
    def resposta_descricao(self,obj):
        return obj.resposta.descricao
    resposta_descricao.admin_order_field = 'resposta'
    resposta_descricao.short_description = 'Resposta Descricao'

admin.site.register(Questao,QuestaoAdmin)
admin.site.register(Unidade)
admin.site.register(Professor)
admin.site.register(Administrativo)
admin.site.register(Disciplina)

