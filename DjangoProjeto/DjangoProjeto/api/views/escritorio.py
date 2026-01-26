from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.escritorio import EscritorioSerializer, EscritorioFullSerializer
from api.views.base_security import BaseSecurity
from digital.models import Escritorio


# Podemos utilizar três classes diferentes :
# customização da listagem e da criação = APIView
# customização apenas da listagem e criação genérica = CreateAPIView
# customização apenas da criação e listagem genérica = ListAPIView

class EscritorioListService(BaseSecurity, APIView):
    queryset = Escritorio.objects.all()

    # Listagem dos escritorios (Método GET do HTTP)
    def get(self, request):
        escritorio = Escritorio.objects.all().order_by('campus', 'predio', 'andar', 'numero')
        context = {
            'request': request
        }
        dados = EscritorioSerializer(escritorio, context=context, many=True)

        return Response(dados.data)

    # Criação de um escritório novo
    def post(self, request):
        try:
            dados = request.data
            contexto = { 'request': request }
            escritorio = EscritorioFullSerializer(
                data=dados, context=contexto
            )
            if escritorio.is_valid():
                escritorio.save()
                return Response(escritorio.data, status=status.HTTP_201_CREATED)
            return Response(escritorio.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as erro:
            return Response(erro, status=status.HTTP_400_BAD_REQUEST)


class EscritorioService(BaseSecurity, APIView):
    queryset = Escritorio.objects.all()

    def get_object(self, pk):
        try:
            return Escritorio.objects.get(pk=pk)
        except Escritorio.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        escritorio = self.get_object(pk)
        contexto = {
            'request': request
        }
        escritorio_serializado = EscritorioFullSerializer(escritorio, context=contexto)

        return Response(escritorio_serializado.data)

    def put(self, request, pk):

        try:
            escritorio = self.get_object(pk)
            novos_dados = request.data
            contexto = { 'request': request }
            escritorio_serializado = EscritorioFullSerializer(
                escritorio, data=novos_dados, context=contexto
            )
            if escritorio_serializado.is_valid():
                escritorio_serializado.save()
                return Response(escritorio_serializado.data)
            return Response(escritorio_serializado.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as erro:
            return Response(erro, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        escritorio = self.get_object(pk)
        escritorio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)