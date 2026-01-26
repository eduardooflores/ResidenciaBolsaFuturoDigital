from django.urls import path

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import saudacao, SaudacaoService, OutraSaudacaoService
from api.views.aluno import AlunoListService
from api.views.atleta import AtletaService
from api.views.calculo import CalculoService
from api.views.conversao_tempo import ConversorTempoService
from api.views.curso import CursoListService, CursoService
from api.views.disciplina import DisciplinaService
from api.views.escritorio import EscritorioListService, EscritorioService
from api.views.exemplo import ExemploListService, ExemploService

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'disciplina', DisciplinaService)
router.register(r'atleta', AtletaService)

urlpatterns = [
    path('saudacao/', saudacao, name="saudacao"),
    path('saudacao/<str:nome>', saudacao, name="saudacao_parametro"),
    path('classe/saudacao/', SaudacaoService.as_view(), name="classe_saudacao"),
    path('classe/outrasaudacao/', OutraSaudacaoService.as_view(), name="classe_outrasaudacao"),
    path('calculo/', CalculoService.as_view(), name="classe_calculo"),
    path('conversao_tempo', ConversorTempoService.as_view(), name="classe_conversor_tempo"),
    path('curso/', CursoListService.as_view(), name="curso-list"),
    path('curso/<int:pk>/', CursoService.as_view(), name="curso_detail"),
    path('exemplo/', ExemploListService.as_view(), name="exemplo-list"),
    path('exemplo/<int:pk>/', ExemploService.as_view(), name="exemplo_detail"),
    path('aluno/', AlunoListService.as_view(), name="aluno-list"),
    path('escritorio/', EscritorioListService.as_view(), name="escritorio-list"),
    path('escritorio/<int:pk>/', EscritorioService.as_view(), name="escritorio-detail"),
    path('auth/', obtain_auth_token),
]

urlpatterns += router.urls