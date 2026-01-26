from datetime import date

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class InicioProjetoValidator:

    def __call__(self, value):
        hoje = date.today()
        if value < hoje:
            raise ValidationError(
                "Data de início inválida! O início do projeto deve ser igual ou maior que hoje.",
                params={"value": value}
            )