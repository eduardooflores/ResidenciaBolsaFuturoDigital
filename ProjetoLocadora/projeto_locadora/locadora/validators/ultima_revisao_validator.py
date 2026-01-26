from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class UltimaRevisaoValidator:
    def __call__(self, value):
        hoje = date.today()
        limite_ano = hoje - relativedelta(years=1)
        if value < limite_ano:
            raise ValidationError(
                "Data de revisão inválida!",
                params={"value": value}
            )