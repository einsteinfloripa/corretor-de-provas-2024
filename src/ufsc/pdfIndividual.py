import pandas as pd
import json
from layoutPDF import create_report
from infos import alunos_infos
from time import sleep
dados_corrigidos = './output/spreadsheets/ranking_de_notas.csv'
df_acertos_por_disciplina = pd.read_csv(dados_corrigidos, dtype={'CPF': str})


# dados_brutos = './assets/Simulinho 2024 - Dados brutos - Sheet1.csv' -->AQUI VAI OS JSON NO LUGAR DA PLANILHA
# df_dados_brutos = pd.read_csv(dados_brutos,dtype={'cpf': str})

# gabarito = './assets/Gabarito Simulinho 2024 - vale - Página1.csv'
# df_gabarito = pd.read_csv(gabarito)





with open("./output/json/media_disciplinas_ufsc.json", 'r', encoding="utf-8") as arquivo:
    media_geral = json.load(arquivo)
    print(media_geral)



with open("./output/json/respostas_brutas_ufsc.json", 'r', encoding="utf-8") as arquivo:
    respostas_brutas = json.load(arquivo)

with open("./output/json/vale ufsc gabarito.json", 'r', encoding="utf-8") as arquivo:
    vale_gabarito = json.load(arquivo)

with open("./output/json/parcias_ufsc.json", 'r', encoding="utf-8") as arquivo:
    parciais_ufsc = json.load(arquivo)


for index, row in df_acertos_por_disciplina.iterrows():
    print(row)
    tabela = []
    data = {}
    cpf_aluno = row["CPF"]
    nome_aluno = row["Nome"]
    data['name'] = nome_aluno
    data['cpf'] = cpf_aluno
    data['objective_score'] = row["total_prova"]
    data['subjects'] = [
        ["Matemática", str(row["Matemática"]), media_geral["Matemática"]],
        ["Português/Literatura", str(row["Português/Literatura"]), media_geral["Português/Literatura"]],
        ["linguagens", str(row["linguagens"]), media_geral["linguagens"]],
        ["Física", str(row["Física"]), media_geral["Física"]],
        ["Química", str(row["Química"]), media_geral["Química"]],
        ["Biologia", str(row["Biologia"]), media_geral["Biologia"]],
        ["Geografia", str(row["Geografia"]), media_geral["Geografia"]],
        ["História", str(row["História"]), media_geral["História"]],
        ["Filosofia/Sociologia", str(row["Filosofia/Sociologia"]), media_geral["Filosofia/Sociologia"]],
        ["Total",str(row["total_prova"]),media_geral["Media de acertos"]]
    ]
    respostas_aluno = respostas_brutas[cpf_aluno]["respostas_do_aluno"]
    for resposta in respostas_aluno:
        resposta_aluno = respostas_aluno[resposta]
        idioma_aluno = respostas_brutas[cpf_aluno]["lingua"]
        disciplina = vale_gabarito[resposta]["Disciplina"]
        gabarito_oficial = vale_gabarito[resposta]["Gabarito"]
        if disciplina == "Inglês":
            disciplina = "linguagens" #gambiarra atras de gambiarra
            if idioma_aluno=="Espanhol": #se a iteração estiver na questão do tema ingles e o idioma_aluno for igual a espanhol
                gabarito_oficial = vale_gabarito[resposta]["Questão Espanhol"] #então gabarito_oficial busca pela resposta espanhol
        #os nomes estão uma merda. A disciplina deveria ser linguagens ou algo do tipo pra fazer mais sentido
        if resposta_aluno == gabarito_oficial:
            resposta_corrigida = f"{resposta_aluno}  ✔"
        else:
            resposta_corrigida = f"{resposta_aluno}  ✖"
        print(disciplina)
        parcial_questao = parciais_ufsc[cpf_aluno]["parcial_aluno"][disciplina][resposta]

        questoes = [resposta,gabarito_oficial, resposta_corrigida, parcial_questao]
        tabela.append(questoes)
    data["idioma_aluno"] = idioma_aluno
    data['questions'] = tabela
    filepdf = f'./output/alunos_relatorios/{cpf_aluno}.pdf'
    create_report(data,filepdf)
        


print(respostas_brutas)