from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from gestao.models import Projeto
from gestao.enumerations.linguagem_programacao import LinguagemProgramacao
from gestao.enumerations.tipo_projeto import TipoProjeto
from gestao.enumerations.status import Status
from api.serializers import ProjetoSerializer


class ProjetosPorLinguagemView(APIView):
    def get(self, request):
        inicio = request.query_params.get("inicio")
        fim = request.query_params.get("fim")
        linguagem = request.query_params.get("linguagem")

        if not inicio or not fim or not linguagem:
            return Response(
                {"erro": "Parâmetros obrigatórios: inicio, fim, linguagem"},
                status=status.HTTP_400_BAD_REQUEST
            )

        inicio = datetime.strptime(inicio, "%Y-%m-%d").date()
        fim = datetime.strptime(fim, "%Y-%m-%d").date()
        linguagem_enum = LinguagemProgramacao[linguagem.strip().upper()]

        projetos = Projeto.objects.listar_projetos_linguagem(inicio, fim, linguagem_enum)

        serializer = ProjetoSerializer(projetos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjetoService(ModelViewSet):
    queryset = Projeto.objects.all().order_by('nome')
    serializer_class = ProjetoSerializer