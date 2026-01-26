from django.db import models

class Status(models.TextChoices):
    PENDING = "Pendente", "Pendente"
    DOING = "Em andamento", "Em andamento"
    DONE = "Concluído", "Concluído"
    BLOCKED = "Bloqueado", "Bloqueado"
    DELAYED = "Atrasado", "Atrasado"