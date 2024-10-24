import pandas as pd
import json
from .layoutPDF import create_report

def gerar_relatorios_individuais(main_path, relatorios_alunos_path, gabarito_vale_convertido):
    print("------------------------------------------------------------------------")
    print("Abrindo arquivos gerados para criar os relatórios individuais")
    
    df_acertos_por_disciplina = pd.read_csv(f"{main_path}/ranking_de_notas.csv", dtype={'CPF': str})

    with open(f"{main_path}/media_disciplinas_ufsc.json", 'r', encoding="utf-8") as arquivo:
        media_geral = json.load(arquivo)

    with open(f"{main_path}/respostas_brutas_ufsc.json", 'r', encoding="utf-8") as arquivo:
        respostas_brutas = json.load(arquivo)

    with open(gabarito_vale_convertido, 'r', encoding="utf-8") as arquivo:
        vale_gabarito = json.load(arquivo)

    with open(f"{main_path}/parcias_ufsc.json", 'r', encoding="utf-8") as arquivo:
        parciais_ufsc = json.load(arquivo)

    print("Gerando relatórios individuais...")
    for index, row in df_acertos_por_disciplina.iterrows():
        tabela = []
        data = {}
        cpf_aluno = row["CPF"]
        nome_aluno = row["Nome"]
        data['name'] = nome_aluno
        data['cpf'] = cpf_aluno
        data['objective_score'] = row["total_prova"]
        
        # Inicializando data['subjects'] de forma dinâmica
        data['subjects'] = []

        # Filtrando colunas que não são disciplinas
        colunas_excluir = ["CPF", "Nome", "total_prova"]

        for coluna in row.index:
            if coluna not in colunas_excluir:
                disciplina = coluna
                valor_estudante = str(row[coluna])
                valor_media = media_geral.get(coluna, "N/A")  # Caso não tenha a média no dicionário

                # Adicionando as disciplinas de forma dinâmica
                data['subjects'].append([disciplina, valor_estudante, valor_media])

        # Adiciona o total de forma separada
        data['subjects'].append([
            "Total", 
            str(row["total_prova"]), 
            media_geral.get("Media de acertos", "N/A")
        ])

        respostas_aluno = respostas_brutas[cpf_aluno]["respostas_do_aluno"]

        for resposta in respostas_aluno:
            resposta_aluno = respostas_aluno[resposta]
            idioma_aluno = respostas_brutas[cpf_aluno]["lingua"]
            disciplina = vale_gabarito[resposta]["Disciplina"]
            gabarito_oficial = vale_gabarito[resposta]["Gabarito"]

            # Tratamento especial para inglês e espanhol
            if disciplina == "Inglês":
                disciplina = "linguagens"
                if idioma_aluno == "Espanhol":
                    gabarito_oficial = vale_gabarito[resposta]["Questão Espanhol"]

            # Verifica se a resposta do aluno está correta
            if resposta_aluno == gabarito_oficial:
                resposta_corrigida = f"{resposta_aluno}  ✔"
            else:
                resposta_corrigida = f"{resposta_aluno}  ✖"

            # Adiciona o valor da parcial da questão
            parcial_questao = parciais_ufsc[cpf_aluno]["parcial_aluno"][disciplina][resposta]

            # Montando a tabela com as questões
            questoes = [resposta, gabarito_oficial, resposta_corrigida, parcial_questao]
            tabela.append(questoes)

        # Adicionando o idioma e as questões no dicionário data
        data["idioma_aluno"] = idioma_aluno
        data['questions'] = tabela

        # Gerando o PDF com o layout específico
        filepdf = f'{relatorios_alunos_path}/{cpf_aluno}.pdf'
        create_report(data, filepdf)

    print("Relatório dos alunos gerados com sucesso!")
    print("------------------------------------------------------------------------")
    print()
    print()
