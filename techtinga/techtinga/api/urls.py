from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import ProjetosPorLinguagemView, TarefasPorProjetoView, TarefasPorColaboradorView, ProjetoService, \
    TarefaService
from .views.relatorio import RelatorioTarefasAnoView

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'projetos', ProjetoService)
router.register(r'tarefas', TarefaService)

urlpatterns = [
    path("projetos/linguagem/", ProjetosPorLinguagemView.as_view(), name="projetos-por-linguagem"),
    path("tarefas/projeto/<str:codigo_projeto>/", TarefasPorProjetoView.as_view(), name="tarefas-por-projeto"),
    path("tarefas/colaborador/<str:responsavel>/", TarefasPorColaboradorView.as_view(), name="tarefas-por-colaborador"),
    path("relatorio/tarefas/<int:ano>/", RelatorioTarefasAnoView.as_view(), name="relatorio-tarefas-ano"),
    path('auth/', obtain_auth_token),
]

urlpatterns += router.urls