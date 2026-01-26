from django.db.models import QuerySet, F
from django.db.models.aggregates import Count, Sum, Avg
from django.db.models.fields import TextField
from django.db.models.functions import Cast
from typing import List, Tuple

from .base_manager import BaseManager
from datetime import date


class VideoManager(BaseManager):

    def publicos(self) -> QuerySet['Video']:
        consulta = self.filter(visibilidade="PUBLICO")
        return consulta

    def privados(self) -> QuerySet['Video']:
        consulta = self.filter(visibilidade="PRIVADO")
        return consulta

    def videos_do_canal(self, canal_youtube_id: str) -> QuerySet['Video']:
        consulta = self.filter(canal__canal_id=canal_id)
        return consulta

    def videos_da_playlist(self, playlist_youtube_id: str) -> QuerySet['Video']:
        consulta = self.filter(playlists__playlist_id=playlist_youtube_id)
        return consulta

    def videos_sem_playlist(self) -> QuerySet['Video']:
        consulta = self.filter(playlists__playlist_nome="")
        return consulta

    def videos_da_categoria(self, categoria_nome: str) -> QuerySet['Video']:
        consulta = self.filter(categorias__nome=categoria_nome)
        return consulta

    def com_qualidade_minima(self, qualidade_min_px: int):
        consulta = self.filter(qualidade_px__gte=qualidade_min_px)
        return consulta

    def postados_entre(self, inicio: date, fim: date) -> QuerySet['Video']:
        consulta = self.filter(data_postagem__range=(inicio, fim))
        return consulta

    def top_por_likes(self, n: int = 10, somente_publicos: bool = True) -> QuerySet['Video']:
        consulta = self.all()
        if somente_publicos:
            consulta = consulta.filter(visibilidade="PUBLICO")
        return consulta.order_by("-likes")[:n]

    def top_por_comentarios(self, n: int = 10) -> QuerySet['Video']:
        consulta = self.all()
        return consulta.order_by("-comentarios")[:n]

    def dislikes_maior_que(self, minimo: int) -> QuerySet['Video']:
        consulta = self.filter(deslikes__gt=minimo)
        return consulta

    def buscar_por_palavra_chave(self, termo: str) -> QuerySet['Video']:
        consulta = self.annotate(
            palavras_chaves_text=Cast("palavras_chaves", TextField())
        ).filter(palavras_chaves_text__icontains=termo)
        return consulta

    def ranking_canais_por_qtd_videos(self, limit: int = 10) -> List[Tuple['str', 'int']]:
        consulta = (
            self.values("canal__canal_nome")
            .annotate(total_videos=Count("id"))
            .order_by("-total_videos")[:limit]
        )
        return [(item["canal__canal_nome"], item["total_videos"]) for item in consulta]

    def ranking_canais_por_soma_likes(self, limit: int = 10) -> List[Tuple['str', 'int']]:
        consulta = (
            self.values("canal__canal_nome")
            .annotate(total_likes=Sum("likes"))
            .order_by("-total_likes")[:limit]
        )
        return [(item["canal__canal_nome"], item["total_likes"]) for item in consulta]

    def ranking_canais_por_media_comentarios(self, limit: int = 10) -> List[Tuple['str', 'float']]:
        consulta = (
            self.values("canal__canal_nome")
            .annotate(media_comentarios=Avg("comentarios"))
            .order_by("-comentarios")[:limit]
        )
        return [(item["canal__canal_nome"], item["media_comentarios"]) for item in consulta]

    def stats_por_qualidade(self) -> List[Tuple['int', 'int', 'float']]:
        consulta = (
            self.values("qualidade_px")
            .annotate(
                total_videos=Count("id"),
                likes_medio=Avg("likes")
            )
        )
        return [(item["qualidade_px"], item["total_videos"], item["likes_medio"]) for item in consulta]

    def stats_por_idioma(self) -> List[Tuple['str', 'int', 'float']]:
        consulta = (
            self.values("idioma")
            .annotate(
                total_videos=Count("id"),
                comentarios_medio=Avg("comentarios")
            )
        )
        return [(item["idioma"], item["total_videos"], item["comentarios_medio"]) for item in consulta]

    def top_categorias_por_videos(self, n: int = 10) -> List[Tuple['str', 'int']]:
        consulta = (
            self.values("categorias__nome")
            .annotate(total_videos=Count("id"))
            .order_by("-total_videos")[:n]
        )
        return [(item["categorias__nome"], item["total_videos"]) for item in consulta]

    def top_por_engajamento(self, n: int = 20, somente_publicos: bool = True) -> QuerySet['Video']:
        consulta = self.all()

        if somente_publicos:
            consulta = consulta.filter(visibilidade="PUBLICO")

        consulta = consulta.annotate(
            engajamento=F("likes") + F("comentarios") + F("salvos")
        ).order_by("-engajamento")[:n]
        return consulta