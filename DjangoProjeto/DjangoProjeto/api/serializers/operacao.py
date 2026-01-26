from typing import Self

from rest_framework import serializers
from api.enumerations import Operador

class OperacaoSerializer(serializers.Serializer):
    primeiro_termo = serializers.FloatField(required=True)
    segundo_termo = serializers.FloatField(required=True)
    operador = serializers.ChoiceField(required=True,
                                       choices=Operador)

    resultado = serializers.FloatField(required=False)

    class Meta:
        # São os fields que serão aproveitados do request
        fields = ['primeiro_termo', 'segundo_termo', 'operador']

    def calcular(self):
        primeiro_termo = self.validated_data.get('primeiro_termo')
        segundo_termo = self.validated_data.get('segundo_termo')
        operador = self.validated_data.get('operador')

        match operador:
            case Operador.ADICAO:
                resultado = primeiro_termo + segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.ADICAO.label})
            case Operador.SUBTRACAO:
                resultado = primeiro_termo - segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.SUBTRACAO.label})
            case Operador.MULTIPLICACAO:
                resultado = primeiro_termo * segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.MULTIPLICACAO.label})
            case Operador.DIVISAO:
                resultado = primeiro_termo / segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.DIVISAO.label})
            case Operador.EXPONENCIACAO:
                resultado = primeiro_termo ** segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": Operador.EXPONENCIACAO.label})
            case Operador.RADICIACAO:
                resultado = primeiro_termo ** (1 / segundo_termo)
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": operador})
            case Operador.PERCENTAGEM:
                resultado = (primeiro_termo / 100) * segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": operador})
            case Operador.MODULO:
                resultado = primeiro_termo % segundo_termo
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operador": operador})
            case _:
                raise NotImplementedError("Operação não implementada")