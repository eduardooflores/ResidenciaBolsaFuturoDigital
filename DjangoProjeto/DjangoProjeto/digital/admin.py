from django.contrib import admin
from digital.models import Exemplo
from digital.models import Atleta
from digital.models import Professor
from digital.models import Escritorio
from digital.models import Aluno
from digital.models import Curso
from digital.models import Disciplina
from digital.models import Historico

# Register your models here.
admin.site.register(Exemplo)
admin.site.register(Atleta)
admin.site.register(Professor)
admin.site.register(Escritorio)
admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Historico)

