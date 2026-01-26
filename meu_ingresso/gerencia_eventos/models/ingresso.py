from django.core.validators import MinLengthValidator, MinValueValidator
from django.db.models import CharField
from django.core.exceptions import ValidationError

from .evento import Evento
from .base_model import BaseModel
from django.db import models
from django.utils import timezone
from datetime import date

from ..enumerations.pagamento import Pagamento
from ..enumerations.tipo_ingresso import TipoIngresso


class Ingresso(BaseModel):
    nome = models.CharField(max_length=150,
                            validators=[MinLengthValidator(10)],
                            verbose_name="Nome do ingresso",
                            help_text="Digite o nome do ingresso")

    email = models.EmailField(verbose_name="E-mail do comprador",
                              help_text="Digite o e-mail do comprador")

    data_compra = models.DateTimeField(default=timezone.now,
                                       verbose_name="Data da compra",
                                       help_text="Data e hora da compra do ingresso")

    preco = models.FloatField(validators=[MinValueValidator(0)],
                              verbose_name="Preço do ingresso",
                              help_text="Digite o preço do ingresso")

    tipo_ingresso = CharField(max_length=20,
                              choices=TipoIngresso.choices,
                              verbose_name="Tipo de ingresso",
                              help_text="Selecione o tipo de ingresso")

    pagamento = CharField(blank=True, null=True,
                          max_length=20,
                          choices=Pagamento.choices,
                          verbose_name="Tipo de pagamento",
                          help_text="Selecione o tipo de pagamento")

    checkin = models.BooleanField(default=False,
                                  verbose_name="Check-in",
                                  help_text="Marque se o ingresso está válido para uso")

    acesso = models.DateTimeField(blank=True, null=True,
                                  verbose_name="Data e hora de acesso",
                                  help_text="Data e hora em que o ingresso foi utilizado")

    evento = models.ForeignKey(Evento,
                               on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (
            f"Nome: {self.nome} | E-mail: {self.email} | Preço: {self.preco:.2f} | Tipo do Ingresso: {self.tipo_ingresso} "
            f"Pagamento: {self.pagamento} | Checkin: {self.checkin} | Acesso: {self.acesso}"
        )

    def clean(self) -> None:
        if self.acesso and self.data_compra is not None:
            if self.acesso < self.data_compra:
                raise ValidationError({
                    "acesso": "A data de acesso não pode ser anterior à compra."
                })

        if self.acesso and self.evento_id:
            data_normalizada = self.acesso.date()

            if data_normalizada > self.evento.data:
                raise ValidationError({
                    "acesso": "A data de acesso não pode ser posterior ao evento."
                })

        if self.checkin and (self.pagamento is None or self.pagamento == ""):
            raise ValidationError({
                "checkin": "Não é possível realizar check-in sem pagamento."
            })

        if self.evento_id and self.evento.ingressos_disponiveis <= 0:
            raise ValidationError({
                "evento": "Não há mais ingresso disponíveis para esse evento."
            })

    def save(self, *args, **kargs) -> None:
        self.full_clean()
        if self.checkin and not self.pagamento:
            raise ValidationError("Não é possível realizar check-in sem pagamento.")

        if self.evento_id:
            if self.evento.ingressos_disponiveis <= 0:
                raise ValidationError("Não há mais ingresso disponíveis para esse evento.")
            if not self.pk:
                self.evento.ingressos_disponiveis -= 1
                self.evento.save(update_fields=["ingressos_disponiveis"])

        if self.evento.ingressos_disponiveis > self.evento.capacidade:
            raise ValidationError("A quantidade de ingresso não pode ultrapassar a capacidade do evento.")
        super().save(*args, **kargs)