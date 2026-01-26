from rest_framework import serializers

from digital.models import Exemplo


class ExemploSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplo
        fields = '__all__'
