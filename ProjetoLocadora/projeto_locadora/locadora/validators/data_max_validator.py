from datetime import date

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class DataMaxValidator:
    def __call__(self, value):
        hoje = date.today()
        if value > hoje:
            raise ValidationError(
                "Data de revisão inválida!",
                params={"value": value}
            )