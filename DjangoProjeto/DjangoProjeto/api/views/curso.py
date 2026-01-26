from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from api.serializers import CursoSerializer
from digital.models import Curso


class CursoListService(ListAPIView, CreateAPIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all().order_by('nome')

class CursoService(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()