from django.db import models


class Predio(models.TextChoices):
    # CONSTANTE = VALOR_NO_DB, VALOR_USUARIO
    TORRE_SUL = "Torre Sul", "Torre Sul"
    TORRE_NORTE = "Torre Norte", "Torre Norte"
    ADM = "Administrativo", "Administrativo"
    A = "Prédio A", "Prédio A"
