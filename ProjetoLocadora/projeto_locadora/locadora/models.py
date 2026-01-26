from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from .enumerations.marca import Marca
from .validators import UltimaRevisaoValidator, DataMaxValidator, IpvaAtrasadoValidator, AnoValidator


class BaseModel(models.Model):

    class Meta:
        abstract = True


class Carro(BaseModel):
    marca = models.CharField(max_length=20,
                             verbose_name="Marca",
                             help_text="Selecione a marca do carro",
                             validators=[MinLengthValidator(4)],
                             choices=Marca)

    modelo = models.CharField(max_length=20,
                              verbose_name="Modelo",
                              help_text="Informe o modelo do carro",
                              validators=[MinLengthValidator(2)])

    ano = models.IntegerField(validators=[AnoValidator()],
                              verbose_name="Ano",
                              help_text="Informe o ano do carro")

    alugado = models.BooleanField(default=False,
                                  verbose_name="Alugado ?",
                                  help_text="Marque se o carro está alugado")

    placa = models.CharField(max_length=7,
                             verbose_name="Placa",
                             help_text="Digite a placa do carro",
                             validators=[MinLengthValidator(7, message="A placa deve conter 7 dígitos")],)

    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2,
                                       validators=[MinValueValidator(200)],
                                       verbose_name="Diária",
                                       help_text="Digite o valor da diária do carro")

    seguro = models.DecimalField(max_digits=10, decimal_places=2,
                                 validators=[MinValueValidator(50)],
                                 verbose_name="Seguro",
                                 help_text="Digite o valor do seguro")

    ultima_revisao = models.DateField(validators=[DataMaxValidator(), UltimaRevisaoValidator()],
                                      verbose_name="Revisão",
                                      help_text="Informe a data da última revisão do carro")

    ipva = models.BooleanField(validators=[IpvaAtrasadoValidator()], default=True,
                               verbose_name="IPVA",
                               help_text="Marque se o IPVA está pago")

    def __str__(self) -> str:
        return (
            f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}"
            f"Alugado: {self.alugado} | Placa: {self.placa} | Valor diária: {self.valor_diaria}"
            f"Seguro: {self.seguro} | Última revisão: {self.ultima_revisao} | IPVA: {self.ipva}"
        )

    def clean(self) -> None:
        valores_minimos = {
            Marca.PORSCHE: 2000,
            Marca.FERRARI: 1500,
            Marca.FORD: 200,
            Marca.LAMBORGHINI: 2000,
            Marca.TESLA: 500,
            Marca.BUGATTI: 5000,
        }

        valor_minimo = valores_minimos.get(self.marca)

        if valor_minimo and self.valor_diaria is not None:
            if valor_minimo and self.valor_diaria < valor_minimo:
                raise ValidationError({
                    "valor_diaria": f"Para {self.get_marca_display()}, o valor mínimo é R$ {valor_minimo}"
                })

        SEGURO = Decimal("0.05")

        if self.valor_diaria is not None:
            valor_seguro = self.valor_diaria * SEGURO

        if self.seguro is not None and self.seguro < valor_seguro:
            raise ValidationError({
                "seguro": f"O valor do seguro deve ser pelo menos R$ {valor_seguro:.2f} (5% da diária)"
            })


    def save(self, *args, **kargs) -> None:
        self.full_clean()
        if self.modelo:
            self.modelo = self.modelo.lower()
        if self.placa:
            self.placa = self.placa.lower()

        super().save(*args, **kargs)