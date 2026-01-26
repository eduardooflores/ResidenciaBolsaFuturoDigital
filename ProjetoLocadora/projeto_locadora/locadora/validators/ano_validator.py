from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class AnoValidator:
    def __call__(self, value):
        hoje = datetime.today()
        ano_atual = hoje.year
        ano_minimo = ano_atual - 5
        ano_maximo = ano_atual + 1

        if value < ano_minimo:
            raise ValidationError(
                "Ano inválido!",
                params={"value": value}
            )

        if value > ano_maximo:
            raise ValidationError(
                "Ano inválido",
                params={"value": value}
            )