from rest_framework import serializers

from digital.models import Escritorio


class EscritorioSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer utilizado para listar os escritorios """

    url = serializers.HyperlinkedIdentityField(
        view_name='api:escritorio-detail', read_only=True, lookup_field='pk'
    )

    class Meta:
        model = Escritorio
        fields = ['url', 'id', 'numero', 'campus']

    def validate(self, kwargs):
        # Podemos customizara validação do serializer aqui, lembre-se de invocar o método full_clean do model se necessário
        return super().validate(kwargs)

class EscritorioFullSerializer(serializers.ModelSerializer):
    """ Serializer utilizado para criação, edição, deleção e recuperação de um objeto """

    class Meta:
        model = Escritorio
        fields = '__all__'

    def create(self, validated_data):
        # Método utilizado para customizar a ação de criação de um objeto
        print(f'Escritório criado: {validated_data}') # validate_data -> dados do objeto criado
        return super().create(validated_data)

    def validate(self, kwargs):
        return super().validate(kwargs)

    def update(self, instance, validated_data):
        # Customizar aqui as ações para atualização no serializer
        print(f'Registro atualizado: {instance}')
        print(f'Novos dados: {validated_data}')
        return super().update(instance, validated_data)