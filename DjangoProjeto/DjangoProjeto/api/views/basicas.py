from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


@api_view(['GET'])
def saudacao(request, nome:str="Aluno"):
    agora = datetime.now()
    mensagem = ""

    if agora.hour >= 6 and agora.hour < 12:
        mensagem = "Bom dia"
    elif agora.hour >= 12 and agora.hour < 18:
        mensagem = "Boa tarde"
    else:
        mensagem = "Boa noite"

    return Response({
        'saudação': f'{mensagem}, {nome}!'
    })


class SaudacaoService(APIView):
    def get(self, request):
        return Response({'mensagem': "Sou uma classe"})

class OutraSaudacaoService(APIView):
    def get(self, request, nome: str = "Aluno"):
        agora = datetime.now()
        mensagem = ""

        if agora.hour >= 6 and agora.hour < 12:
            mensagem = "Bom dia"
        elif agora.hour >= 12 and agora.hour < 18:
            mensagem = "Boa tarde"
        else:
            mensagem = "Boa noite"

        return Response({
            'saudação': f'{mensagem}, {nome}!'
        })