from django.db import models

class Modalidade(models.TextChoices):
    EAD = "EAD", "EAD"
    SEMI_PRESENCIAL = "SEMI-PRESENCIAL", "SEMI-PRESENCIAL"
    PRESENCIAL = "PRESENCIAL", "PRESENCIAL"