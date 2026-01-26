from datetime import date

from django.core.exceptions import ValidationError


def validar_maioridade(valor):
    try:
        hoje = date.today()
        minimo = hoje.replace(year=hoje.year - 18)
        if valor > minimo:
            raise ValidationError(
                "Idade miníma não atingida",
                params={"valor": valor}
            )


    except ValueError as e:
        print(e)