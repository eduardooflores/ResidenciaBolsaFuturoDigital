from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from gestao.models import Projeto


class ProjetoMinimalSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        try:
            projeto = Projeto(**attrs)
            projeto.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e)
        return attrs

class ProjetoSerializer(ProjetoMinimalSerializer):
    class Meta:
        model = Projeto
        fields = ['codigo', 'nome', 'cliente']