from rest_framework import serializers

from api.enumerations import Tempo


class ConversaoSerializer(serializers.Serializer):
    tempo = serializers.FloatField(required=True)

    unidade_tempo_inicial = serializers.ChoiceField(required=True, choices=Tempo)

    unidade_tempo_final = serializers.ChoiceField(required=True, choices=Tempo)

    resultado = serializers.FloatField(required=False)

    class Meta:
        fields = ['tempo', 'unidade_tempo_inicial', 'unidade_tempo_final']

    UNIDADES_TEMPO_SEGUNDOS = {
        Tempo.SEGUNDO: 1,
        Tempo.MINUTO: 60,
        Tempo.HORA: 3600,
        Tempo.DIA: 86400,
        Tempo.SEMANA: 604800,
        Tempo.MES: 2592000, # 30 DIAS em todos os meses
        Tempo.ANO: 31536000, # 365 DIAS
    }

    def converter(self):
        tempo = self.validated_data.get('tempo')
        unidade_tempo_inicial = self.validated_data.get('unidade_tempo_inicial')
        unidade_tempo_final = self.validated_data.get('unidade_tempo_final')

        em_segundos = tempo * self.UNIDADES_TEMPO_SEGUNDOS[unidade_tempo_inicial]
        resultado = em_segundos / self.UNIDADES_TEMPO_SEGUNDOS[unidade_tempo_final]
        self.validated_data.update({"resultado": resultado})