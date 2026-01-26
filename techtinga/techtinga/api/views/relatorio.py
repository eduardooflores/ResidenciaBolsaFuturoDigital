from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models
from gestao.models import Projeto, Tarefa
from gestao.enumerations.status import Status


class RelatorioTarefasAnoView(APIView):

    def get(self, request, ano):
        relatorio = {
            "ano": ano,
            "projetos": []
        }

        projetos = Projeto.objects.filter(
            models.Q(tarefas__criacao__year=ano) | models.Q(tarefas__conclusao__year=ano)
        ).distinct()

        for projeto in projetos:
            tarefas = Tarefa.objects.filter(projeto=projeto).filter(
                models.Q(criacao__year=ano) | models.Q(conclusao__year=ano)
            )

            if not tarefas.exists():
                continue

            resumo = {}
            for status in Status:
                status_valor = status.value
                tarefas_status = tarefas.filter(status=status_valor)

                resumo[status.name] = {
                    "quantidade": tarefas_status.count(),
                    "horas_estimadas": sum(t.estimativa_horas or 0 for t in tarefas_status),
                    "horas_registradas": sum(t.horas_registradas or 0 for t in tarefas_status),
                    "tarefas": [
                        {
                            "titulo": t.titulo,
                            "linguagem": t.linguagem,
                            "estimativa_horas": t.estimativa_horas,
                            "horas_registradas": t.horas_registradas,
                            "status": t.status,
                            "responsavel": t.responsavel,
                            "criacao": t.criacao,
                            "conclusao": t.conclusao,
                        }
                        for t in tarefas_status
                    ]
                }

            relatorio["projetos"].append({
                "nome": projeto.nome,
                "inicio": projeto.inicio,
                "previsao_termino": projeto.previsao_termino,
                "orcamento": projeto.orcamento,
                "resumo": resumo
            })

        return Response(relatorio)
