from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from digital.models import Aluno


class AlunoMinimalSerializer(serializers.ModelSerializer):

    def validate(self, kwargs):
        try:
            aluno = Aluno(**kwargs)
            aluno.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e)
        return kwargs

class AlunoSerializer(AlunoMinimalSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome']

class AlunoDetailedSerializer(AlunoMinimalSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'