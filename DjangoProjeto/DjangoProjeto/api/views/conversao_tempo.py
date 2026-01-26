from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from api.serializers.conversao import ConversaoSerializer


class ConversorTempoService(APIView):
    def get(self, request):
        dados = ConversaoSerializer()
        return Response(dados.data, status=status.HTTP_200_OK)

    def post(self, request):
        dados = JSONParser().parse(request)
        dados_serializados = ConversaoSerializer(data=dados)
        if dados_serializados.is_valid():
            dados_serializados.converter()
            return Response(dados_serializados.data, status=status.HTTP_200_OK)
        else:
            return Response(dados_serializados.errors, status=status.HTTP_400_BAD_REQUEST)