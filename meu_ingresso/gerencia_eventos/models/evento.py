from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from gerencia_eventos.enumerations.tipo_evento import TipoEvento
from .base_model import BaseModel
from django.db import models
from django.utils import timezone

class Evento(BaseModel):
    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(5)],
                            verbose_name="Nome",
                            help_text="Digite o nome do evento")

    descricao = models.TextField(validators=[MinLengthValidator(0), MaxLengthValidator(1000)],
                                 blank=True, null=True,
                                 verbose_name="Descrição",
                                 help_text="Digite a descrição do evento")

    data = models.DateField(default=timezone.now,
                            verbose_name="Data evento",
                            help_text="Digite a data do evento")

    time = models.TimeField(default=timezone.now,
                            verbose_name="Hora evento",
                            help_text="Digite a hora do evento")

    tipo_evento = models.CharField(max_length=20,
                                   choices=TipoEvento.choices,
                                   verbose_name="Tipo evento",
                                   help_text="Escolha o tipo de evento")

    capacidade = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(60000)],
                                     verbose_name="Capacidade evento",
                                     help_text="Digite a capacidade do evento")

    cobertura_campo = models.BooleanField(default=False,
                                          verbose_name="Evento tem cobertura",
                                          help_text="Marque se o evento possui uma cobertura")

    organizador = models.CharField(max_length=100,
                                   validators=[MinLengthValidator(5)],
                                   verbose_name="Organizador do evento",
                                   help_text="Digite o nome do organizador do evento")

    ingressos_disponiveis = models.IntegerField(validators=[MinValueValidator(0)],
                                                verbose_name="Ingressos disponíveis",
                                                help_text="Digite a quantidade de ingressos disponíveis")


    def __str__(self) -> str:
        return (
            f"Nome: {self.nome} | Data: {self.data} | Hora: {self.time} | Tipo: {self.tipo_evento} "
            f"Capacidade: {self.capacidade} | Cobertura: {self.cobertura_campo} | Organizador: {self.organizador} | "
            f"Ingressos disponíveis: {self.ingressos_disponiveis}"
        )

    def clean(self):
        if self.ingressos_disponiveis and self.capacidade is not None:
            if self.ingressos_disponiveis > self.capacidade:
                raise ValidationError({
                    "ingressos_disponiveis": f"A quantidade de ingressos disponíveis não pode ultrapassar a capacidade do evendo. CAPACIDADE {self.capacidade}"
                })