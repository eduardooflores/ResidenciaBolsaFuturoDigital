from django.db import models

class Idioma(models.TextChoices):
    PORTUGUES_BRASILEIRO = "pt-BR", "Portugues (Brasil)"
    PORTUGUES_PORTUGAL = "pt-PT", "Portugues"
    ESPANHOL = "es", "Espanhol"
    INGLES = "en", "Ingles"