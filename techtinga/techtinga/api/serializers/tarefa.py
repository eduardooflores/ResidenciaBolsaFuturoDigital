from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from gestao.models import Tarefa



class TarefaMinimalSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        try:
            tarefa = Tarefa(**attrs)
            tarefa.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e)
        return attrs

class TarefaSerializer(TarefaMinimalSerializer):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'responsavel', 'status', 'criacao']