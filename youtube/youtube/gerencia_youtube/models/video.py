from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator

from .base_model import BaseModel
from django.db import models

from .canal import Canal
from .categoria import Categoria
from .playlist import Playlist
from ..enumerations.idioma import Idioma
from ..enumerations.qualidade import Qualidade
from ..enumerations.visibilidade import Visibilidade
from ..managers.video_manager import VideoManager


class Video (BaseModel):
    video_id = models.CharField(max_length=20,
                                validators=[MinLengthValidator(5)],
                                verbose_name="ID do vídeo",
                                help_text="Digite o ID do vídeo.")


    url = models.CharField(max_length=100,
                           validators=[MinLengthValidator(40)],
                           verbose_name="URL do vídeo",
                           help_text="Digite a URL do vídeo.")

    titulo = models.CharField(max_length=100,
                              validators=[MinLengthValidator(10)],
                              verbose_name="Título do Vídeo",
                              help_text="Digite o título do vídeo.")

    likes = models.IntegerField(validators=[MinValueValidator(0)],
                                verbose_name="Likes do Vídeo",
                                help_text="Digite a quantidade de likes do vídeo.")

    deslikes = models.IntegerField(validators=[MinValueValidator(0)],
                                   verbose_name="Deslikes do Vídeo",
                                   help_text="Digite a quantidade de deslikes do vídeo.")

    salvos = models.IntegerField(validators=[MinValueValidator(0)],
                                 verbose_name="Salvos do vídeo",
                                 help_text="Digite a quantas vezes o vídeo foi salvo.")

    downloads = models.IntegerField(validators=[MinValueValidator(0)],
                                    verbose_name="Downloads do Vídeo",
                                    help_text="Digite a quantidade de vezes que p vídeo foi baixado.")

    duracao = models.TimeField(auto_now=False, auto_now_add=False,
                               verbose_name="Duração do Vídeo",
                               help_text="Digite a duração do vídeo")

    comentarios = models.IntegerField(validators=[MinValueValidator(0)],
                                      verbose_name="Comentários do vídeo",
                                      help_text="Digite a quantidade de comentários do vídeo")

    qualidade_px = models.CharField(max_length=4,
                                    verbose_name="Qualidade",
                                    help_text="Selecione a qualidade do vídeo",
                                    validators=[MinLengthValidator(3)],
                                    choices=Qualidade.choices)

    palavras_chaves = models.JSONField(verbose_name="Palavras-chave",
                                       help_text="Digite as palavras-chave do vídeo")

    descricao = models.TextField(validators=[MaxLengthValidator(1000)],
                                 blank=True,
                                 verbose_name="Descrição do Vídeo",
                                 help_text="Digite a descrição do vídeo")

    data_postagem = models.DateField(auto_now=False, auto_now_add=False,
                                     verbose_name="Data da postagem",
                                     help_text="Digite a data da postagem do vídeo")

    idioma = models.CharField(max_length=5,
                              verbose_name="Idioma",
                              help_text="Selecione o idioma do vídeo",
                              validators=[MinLengthValidator(2)],
                              choices=Idioma.choices)

    visibilidade = models.CharField(max_length=7,
                                    verbose_name="Visibilidade",
                                    help_text="Selecione a visibilidade do vídeo",
                                    validators=[MinLengthValidator(7)],
                                    choices=Visibilidade.choices)

    canal = models.ForeignKey(Canal,
                              on_delete=models.CASCADE,
                              verbose_name="Canal",
                              help_text="Selecione o canal")

    categorias = models.ManyToManyField(Categoria,
                                       verbose_name="Categorias",
                                        help_text="Selecione as categorias")

    playlists = models.ManyToManyField(Playlist,
                                       verbose_name="Playlist",
                                       help_text="Selecione uma playlist")

    objects = VideoManager()

    def __str__(self):
        categorias = ", ".join(self.categorias.values_list("nome", flat=True))
        return (f"{self.video_id} - {self.url} - {self.titulo} - Categoria:{categorias} - Likes: {self.likes} - Deslikes: {self.deslikes} "
                f"Salvos: {self.salvos} - Downloads: {self.downloads} - Duração:{self.duracao} - Comentários: {self.comentarios} "
                f"Qualidade:{self.qualidade_px} - {self.idioma} - {self.visibilidade} - {self.canal}")