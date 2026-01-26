from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from gestao.models import Projeto, Tarefa
from api.serializers import TarefaSerializer

class TarefasPorProjetoView(APIView):
    def get(self, request, codigo_projeto):
        try:
            projeto = Projeto.objects.get(codigo=codigo_projeto)
            tarefas = Tarefa.objects.listar_tarefas_projeto(projeto)
            serializer = TarefaSerializer(tarefas, many=True)
            return Response(serializer.data)
        except Projeto.DoesNotExist:
            return Response({"erro": "Projeto não encontrado"}, status=status.HTTP_404_NOT_FOUND)


class TarefasPorColaboradorView(APIView):
    def get(self, request, responsavel):
        tarefas = Tarefa.objects.listar_tarefas_colaborador(responsavel)
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

class TarefaService(ModelViewSet):
    queryset = Tarefa.objects.all().order_by('criacao')
    serializer_class = TarefaSerializer