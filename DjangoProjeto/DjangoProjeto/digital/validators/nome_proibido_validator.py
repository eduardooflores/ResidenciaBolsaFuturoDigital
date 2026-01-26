from django.utils.deconstruct import deconstructible


@deconstructible
class NomeProibidoValidator:


    def __init__(self, nomes_proibidos=[]):
        if not isinstance(nomes_proibidos, list):
            raise TypeError("Parâmetro deve ser uma lista")

        self.nomes_proibidos = nomes_proibidos

    # Aqui definimos a lógica do validador
    def __call__(self, valor):
        if valor in self.nomes_proibidos:
            raise ValidationError(
                "Nome proibido",
                params={"valor": valor}
            )

    # Este método permite que várias instâncias dessa classe sejam criadas ou reutiliza a mesma instância
    def __eq__(self, other):
        return(
            isinstance(other, NomeProibidoValidator)
            and self.nomes_proibidos == other.nomes_proibidos
        )