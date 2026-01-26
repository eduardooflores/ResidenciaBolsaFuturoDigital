from django.db import models


class Status(models.TextChoices):
    EM_ANDAMENTO = "Em andamento", "Em andamento"
    REPROVADO_NOTA = "Reprovado por nota", "Reprovado por nota"
    REPROVADO_FREQUENCIA = "Reprovado por frequência", "Reprovado por frequência"
    APROVADO = "Aprovado", "Aprovado"
    APROVADO_EXAME = "Aprovado por exame", "Aprovado por exame"
    EM_EXAME = "Em exame", "Em exame"