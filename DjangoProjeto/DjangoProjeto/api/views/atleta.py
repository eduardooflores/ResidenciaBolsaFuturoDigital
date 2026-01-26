from rest_framework.viewsets import ModelViewSet

from api.serializers import AtletaSerializer
from digital.models import Aluno


class AtletaService(ModelViewSet):
    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AtletaSerializer