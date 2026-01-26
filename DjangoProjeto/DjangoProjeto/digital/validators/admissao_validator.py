from datetime import date

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AdmissaoValidator:

    def __call__(self, value):
        hoje = date.today()
        print(hoje, value)
        if value > hoje:
            raise ValidationError(
                "Data de admissão inválida",
                params={"value": value}
            )
