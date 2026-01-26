from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from .ingresso import Ingresso
from .base_model import BaseModel
from ..enumerations.setor import Setor


class Assento(BaseModel):
    codigo = models.CharField(max_length=3,
                              validators=[MinLengthValidator(3)],
                              verbose_name="Código do assento",
                              help_text="Digite o código do assento")

    bloco = models.IntegerField(validators=[MinValueValidator(1)],
                                verbose_name="Bloco do assento",
                                help_text="Digite o número do bloco onde o assento está localizado")

    setor = models.CharField(max_length=20,
                             choices=Setor.choices,
                             verbose_name="Setor do assento",
                             help_text="Selecione o setor do assento")

    disponivel = models.BooleanField(default=False,
                                     verbose_name="Assento disponível",
                                     help_text="Marque se o assento está disponível")

    preco = models.FloatField(validators=[MinValueValidator(0.00)],
                              verbose_name="Valor do assento",
                              help_text="Digite o valor do assento")

    acessibilidade = models.BooleanField(default=False,
                                         verbose_name="Acessível",
                                         help_text="Marque se o assento possui acessibilidade")

    ultima_manutencao = models.DateField(null=True, blank=True,
                                         verbose_name="Data da última manutenção",
                                         help_text="Digite a data da última manutenção")

    ingresso = models.OneToOneField(Ingresso,
                                    on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo} | Bloco: {self.bloco} | Setor: {self.setor} | Disponível: {self.disponivel} "
            f"Preço: {self.preco} | Acessibilidade: {self.acessibilidade} | Última manutenção: {self.ultima_manutencao}"
        )

    def save(self, *args, **kwargs):
        if self.ingresso:
            self.disponivel = False
        else:
            self.disponivel = True
        
        super().save(*args, **kwargs)