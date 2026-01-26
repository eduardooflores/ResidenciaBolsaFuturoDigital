import csv
from decimal import Decimal
from django.core.exceptions import ValidationError
from gerencia_youtube.models import Video, Canal, Categoria, Playlist
from datetime import datetime

total = 0
erros = 0

with open("youtube_videos_nao_normalizado.csv", "r", encoding="utf-8") as arquivo:
    try:
        reader = csv.reader(arquivo, delimiter=",", quotechar='"')
        next(reader)  # pula o cabeçalho
        for dados in reader:
            try:
                video_id = dados[0]

                url = dados[1]
                if not url.startswith("http"):
                    url = "https://" + url
                if len(url) < 40:
                    print(f"URL inválida: {url} — registro excluído")
                    erros += 1
                    continue

                titulo = dados[2].strip()
                if titulo == "":
                    print(f"Titulo inválido: {titulo} - registro excluído")
                    erros += 1
                    continue

                try:
                    likes = int(dados[3].replace(".", "").replace(",", "").strip())
                    if likes < 0:
                        likes = 0
                except ValueError:
                    likes = 0

                try:
                    dislikes = int(dados[4].replace(".", "").replace(",", "").strip())
                    if dislikes < 0:
                        dislikes = 0
                except ValueError:
                    dislikes = 0

                try:
                    salvos = int(dados[5].replace(".", "").replace(",","".strip()))
                    if salvos < 0:
                        salvos = 0
                except ValueError:
                    salvos = 0

                try:
                    downloads = int(dados[6])
                    if downloads < 0:
                        downloads = 0
                except ValueError:
                    print(f"Tipo inválido: {downloads} - registro excluído")
                    erros += 1
                    continue

                duracao = dados[7].strip()

                try:
                    datetime.strptime(duracao, "%H:%M:%S").time()
                except ValueError:
                    print(f"Duração inválida: {duracao} — registro excluído")
                    erros += 1
                    continue

                try:
                    comentarios = int(dados[8].replace(".", "").replace(",", "").strip())
                    if comentarios < 0:
                        comentarios = 0
                except ValueError:
                    comentarios = 0

                qualidade_px = dados[9].replace("px", "").replace("P", "").replace("p", "").strip()
                if not qualidade_px:
                    qualidade_px = "720"
                if qualidade_px == "" or qualidade_px == "0":
                    qualidade_px = "720"

                canal_id = dados[10]
                canal_nome = dados[11].strip()
                canal_inscritos = int(dados[12])

                categorias = dados[13].split(";")
                palavras_chave = dados[14].split(";")

                descricao = dados[15]
                raw_date = dados[16].strip().replace("“", "").replace("”", "").replace('"', '')

                try:
                    data_postagem = datetime.strptime(dados[16].strip(), "%Y-%m-%d").date()
                except ValueError:
                    print(f"Data inválida: {dados[16]} — registro excluído")
                    erros += 1
                    continue

                visibilidade = dados[17].strip().upper()
                if visibilidade == "PÚBLICO":
                    visibilidade = "PUBLICO"

                playlist_id = dados[18]
                playlist_nome = dados[19]

                idioma = dados[20].strip().lower()
                idiomas = {
                    "pt-br": "pt-BR",
                    "ptbr": "pt-BR",
                    "portugues": "pt-BR",
                    "": "pt-BR",
                    "en-us": "en",
                    "en": "en",
                    "es-es": "es",
                    "es": "es",
                }
                idioma = idiomas.get(idioma, "pt-BR")


                canal, _ = Canal.objects.get_or_create(
                    canal_id=canal_id,
                    defaults={"canal_nome": canal_nome, "canal_inscritos": canal_inscritos}
                )

                playlist, _ = Playlist.objects.get_or_create(
                    playlist_id=playlist_id,
                    defaults={"playlist_nome": playlist_nome}
                )

                video = Video(
                    video_id=video_id,
                    url=url,
                    titulo=titulo,
                    likes=likes,
                    deslikes=dislikes,
                    salvos=salvos,
                    downloads=downloads,
                    duracao=duracao,
                    comentarios=comentarios,
                    qualidade_px=qualidade_px,
                    palavras_chaves=palavras_chave,
                    descricao=descricao,
                    data_postagem=data_postagem,
                    idioma=idioma,
                    visibilidade=visibilidade,
                    canal=canal
                )
                video.full_clean()
                video.save()

                for nome in categorias:
                    nome = nome.strip()
                    if nome:
                        categoria, _ = Categoria.objects.get_or_create(nome=nome)
                        video.categorias.add(categoria)

                video.playlists.add(playlist)

                print(f"Registro importado: {video_id}")
                total += 1

            except Exception as e:
                print(f"Erro: {e} na linha: {dados}")
                erros += 1

    except Exception as e:
        print(f"Erro geral: {e}")

print(f"\nImportação concluída: {total} vídeos importados, {erros} erros.")
