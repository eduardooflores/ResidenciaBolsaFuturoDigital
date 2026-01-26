import csv
from datetime import datetime
from django.core.exceptions import ValidationError
from gestao.models import Projeto, Tarefa

total = 0
erros = 0

with open("techtinga.csv", "r", encoding="utf-8") as arquivo:
    try:
        reader = csv.reader(arquivo, delimiter=",", quotechar='"')
        next(reader)
        for dados in reader:
            try:
                projeto_codigo = dados[0]
                projeto_nome = dados[1]
                projeto_tipo = dados[2]
                projeto_cliente = dados[3]
                projeto_gerente = dados[4]

                projeto_inicio = datetime.strptime(dados[5], "%Y-%m-%d").date()

                projeto_previsao = None
                if dados[6].strip():
                    projeto_previsao = datetime.strptime(dados[6], "%Y-%m-%d").date()

                projeto_fim = None
                if dados[7].strip():
                    projeto_fim = datetime.strptime(dados[7], "%Y-%m-%d").date()

                projeto_orcamento = float(dados[8])

                ativo = dados[9].strip().lower() == "true"
                if not ativo:
                    print(f"Projeto {projeto_codigo} está desativado — registro excluído")
                    erros += 1
                    continue

                tarefa_titulo = dados[10].strip()
                if tarefa_titulo == "":
                    print(f"Tarefa sem título no projeto {projeto_codigo} — registro ignorado")
                    erros += 1
                    continue

                tarefa_descricao = dados[11]

                tarefa_linguagem_row = dados[12].strip().lower()
                linguagens = {
                    "php": "Php",
                    "python": "Python",
                    "javascript": "JavaScript",
                    "js": "JavaScript",
                    "java": "Java",
                    "c#": "C#",
                    "csharp": "C#",
                    "c++": "C++",
                    "c": "C",
                    "dart": "Dart",
                    "cplusplus": "C++",
                }
                tarefa_linguagem = linguagens.get(tarefa_linguagem_row)
                if tarefa_linguagem is None:
                    print(f"Linguagem inválida: {tarefa_linguagem_row} — registro excluído")
                    erros += 1
                    continue

                tarefa_estimativa = int(dados[13]) if dados[13].strip() else 0
                if tarefa_estimativa < 0:
                    tarefa_estimativa = 0

                tarefa_horas = int(dados[14]) if dados[14].strip() else 0

                tarefa_prioridade = int(dados[15]) if dados[15].strip() else 1
                if tarefa_prioridade < 1:
                    tarefa_prioridade = 1
                if tarefa_prioridade > 5:
                    tarefa_prioridade = 5

                tarefa_status_row = dados[16].strip().lower()
                status = {
                    "delayed": "Atrasado",
                    "pending": "Pendente",
                    "done": "Concluído",
                    "blocked": "Bloqueado",
                    "doing": "Em andamento",
                    "finished": "Concluído",
                }
                tarefa_status = status.get(tarefa_status_row)
                if tarefa_status is None:
                    print(f"Status inválido: {tarefa_status_row} - registro excluído")
                    erros += 1
                    continue

                tarefa_responsavel = dados[17]

                tarefa_criacao = None
                if dados[18].strip():
                    try:
                        tarefa_criacao = datetime.strptime(dados[18].strip(), "%Y-%m-%dT%H:%M:%S")
                    except ValueError:
                        tarefa_criacao = datetime.strptime(dados[18].strip(), "%d/%m/%Y")

                tarefa_conclusao = None
                if dados[19].strip():
                    try:
                        tarefa_conclusao = datetime.strptime(dados[19].strip(), "%Y-%m-%dT%H:%M:%S")
                    except ValueError:
                        tarefa_conclusao = datetime.strptime(dados[19].strip(), "%d/%m/%Y")

                if tarefa_conclusao and tarefa_criacao and tarefa_conclusao < tarefa_criacao:
                    print(f"Ajuste: conclusão {tarefa_conclusao} anterior à criação {tarefa_criacao}, substituída por None")
                    tarefa_conclusao = None

                projeto, _ = Projeto.objects.get_or_create(
                    codigo=projeto_codigo,
                    defaults={
                        "nome": projeto_nome,
                        "tipo_projeto": projeto_tipo,
                        "cliente": projeto_cliente,
                        "gerente": projeto_gerente,
                        "inicio": projeto_inicio,
                        "previsao_termino": projeto_previsao,
                        "fim": projeto_fim,
                        "orcamento": projeto_orcamento,
                        "ativo": ativo,
                    }
                )

                tarefa = Tarefa(
                    titulo=tarefa_titulo,
                    descricao=tarefa_descricao,
                    linguagem=tarefa_linguagem,
                    estimativa_horas=tarefa_estimativa,
                    horas_registradas=tarefa_horas,
                    prioridade=tarefa_prioridade,
                    status=tarefa_status,
                    responsavel=tarefa_responsavel,
                    criacao=tarefa_criacao,
                    conclusao=tarefa_conclusao,
                    projeto=projeto
                )
                tarefa.full_clean()
                tarefa.save()

                print(f"Registro importado: Projeto {projeto_codigo} | Tarefa {tarefa_titulo}")
                total += 1

            except Exception as e:
                print(f"Erro: {e} na linha: {dados}")
                erros += 1

    except Exception as e:
        print(f"Erro geral: {e}")

print(f"\nImportação concluída: {total} registros importados, {erros} erros.")
