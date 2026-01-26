from rest_framework import serializers
from digital.models import Disciplina

class DisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:disciplina-detail"
    )

    class Meta:
        model = Disciplina
        fields = '__all__'