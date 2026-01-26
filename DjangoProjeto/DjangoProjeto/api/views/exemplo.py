from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from api.serializers import ExemploSerializer
from digital.models import Exemplo


class ExemploListService(ListAPIView, CreateAPIView):
    serializer_class = ExemploSerializer
    queryset = Exemplo.objects.all().order_by('nome')

class ExemploService(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = ExemploSerializer
    queryset = Exemplo.objects.all()