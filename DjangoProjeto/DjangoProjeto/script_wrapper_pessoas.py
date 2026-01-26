from decimal import Decimal

from django.core.exceptions import ValidationError

from manage import *
import contextlib, io

saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()

from wrapper.models import Pessoa, Cidade, Esporte, Time
from wrapper.enumerations import Genero

cidades = set(Cidade.objects.all())
esportes = set(Esporte.objects.all())
times = set(Time.objects.all())

total = 0
erros = 0

with open('pessoas.csv', 'r', encoding="utf-8") as arquivo:
    try:
        arquivo.readline()
        for linha in arquivo:
            dados = linha.split(',')
            nome = dados[0]
            genero = dados[1]
            idade = int(dados[2])
            cidade = dados[3]
            estado = dados[4]
            time = dados[5]
            renda = Decimal(dados[6])
            esporte = dados[7]

            if genero.lower() == 'feminino':
                genero = Genero.FEMININO
            elif genero.lower() == 'masculino':
                genero = Genero.MASCULUNO
            else:
                genero = Genero.OUTRO

            try:
                # CONSULTA A CIDADE
                endereco = Cidade.objects.get(nome=cidade, estado=estado)
            except Cidade.DoesNotExist:
                try:
                    # CADASTRA A CIDADE
                    endereco = Cidade(nome=cidade, estado=estado)
                    endereco.full_clean()
                    endereco.save()
                except ValidationError as e:
                    print(e)

            # CONSULTA SE O CLUBE EXISTE NA BASE
            clube = Time.objects.filter(nome=time)

            if len(clube) == 0:
                try:
                    # CASO NÃO EXISTE E CRIA
                    clube = Time(nome=time)
                    clube.full_clean()
                    clube.save()
                except ValidationError as e:
                    print(e)
            # SE EXISTIR MAIS DE UM ADICIONA AO PRIMIERO QUE APARECE
            elif len(clube) >= 1:
                clube = clube[0]

            esporte_favorito = Esporte.objects.filter(nome=esporte)

            if len(esporte_favorito) == 0:
                try:
                    esporte_favorito = Esporte(nome=esporte)
                    esporte_favorito.full_clean()
                    esporte_favorito.save()
                except ValidationError as e:
                    print(e)
            elif len(esporte_favorito) >= 1:
                esporte_favorito = esporte_favorito[0]

            try:
                nova_pessoa = Pessoa(
                    nome=nome,
                    genero=genero,
                    idade=idade,
                    renda=renda,
                    endereco=endereco,
                    time=clube,
                    esporte=esporte_favorito
                )
                nova_pessoa.full_clean()
                nova_pessoa.save()
                print(f"Registro processado: {linha}")
                total += 1
            except:
                print(f"Problem: {linha}")
    except Exception as e:
        print(f"Problema: {e} com o registro {linha}")
        erros += 1

print(f"Processamento concluído com {total} processados e {erros} erros")