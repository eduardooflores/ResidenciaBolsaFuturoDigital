from django.core.serializers import serialize
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from api.serializers import AlunoSerializer, AlunoDetailedSerializer
from digital.models import Aluno


class AlunoListService(ListAPIView):

    def get_queryset(self):
        try:
            alunos = Aluno.objects.all()
            nome = self.request.GET.get("nome")
            matricula = self.request.GET.get("matricula")
            if nome and matricula:
                alunos = Aluno.objects.find_by_name_and_matricula(nome, matricula)
                AlunoListService.serializer_class = AlunoDetailedSerializer

            elif nome != None:
                alunos = Aluno.objects.find_by_name(nome)
                AlunoListService.serializer_class = AlunoDetailedSerializer

            elif matricula != None:
                alunos = Aluno.objects.find_by_matricula(matricula)
                AlunoListService.serializer_class = AlunoDetailedSerializer
            else:
                AlunoListService.serializer_class = AlunoSerializer
            return alunos

        except Exception as e:
            raise serializers.ValidationError(e)