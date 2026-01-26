from ctypes.wintypes import HENHMETAFILE

from digital.enumerations import Status
from digital.models import BaseModel, Disciplina, Aluno
from django.db import models

class Historico(BaseModel):
    aluno = models.ForeignKey(Aluno, on_delete=models.RESTRICT,
                              verbose_name="Aluno",
                              help_text="Selecione um aluno")

    disciplina = models.ForeignKey(Disciplina, on_delete=models.RESTRICT,
                                   verbose_name="Disciplina",
                                   help_text="Seleciona uma disciplina")

    ingresso = models.DateField(verbose_name="Ingresso",
                                help_text="Data de ingresso do aluna na disciplina")
                                # TODO: criar validador para data de ingresso maior que a data da disciplina

    fim = models.DateField(verbose_name="Fim",
                           help_text="Data de encerramento do hstorico do aluno")
                           # TODO: criar um validador para data de fim ser menor que da disciplina

    nota = models.DecimalField(max_digits=4,
                               decimal_places=2,
                               verbose_name="TESTE",
                               help_text="Nota do aluno na disciplina")

    presenca = models.FloatField(verbose_name="Frequência",
                                 help_text="Percemtual de frequência do aluno, entre 0--100")

    status = models.CharField(max_length=30,
                              verbose_name="Status",
                              help_text="Selecione o status do aluno na disciplina",
                              choices=Status, default=True)