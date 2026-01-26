from rest_framework import serializers

from digital.models import Aluno


class AtletaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:aluno-detail"
    )

    class Meta:
        model = Aluno
        fields = '__all__'