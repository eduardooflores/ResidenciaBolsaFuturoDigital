from rest_framework.viewsets import ModelViewSet

from api.serializers.disciplina import DisciplinaSerializer
from digital.models import Disciplina


class DisciplinaService(ModelViewSet):
    queryset = Disciplina.objects.all().order_by('nome')
    serializer_class = DisciplinaSerializer