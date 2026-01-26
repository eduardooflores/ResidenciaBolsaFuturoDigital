from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class IpvaAtrasadoValidator:
    def __call__(self, value):
        if value == False:
            raise ValidationError(
                "O IPVA não pode estar atrasado!",
                params={"value": value}
            )