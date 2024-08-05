import pandas as pd
import json

df_ufsc = pd.read_csv("./assets/spreadsheets/Cópia de SimuUFSC 2024 - Dados brutos.xlsx - Sheet1.csv")
total_de_linhas = df_ufsc.shape[0]

respostas_brutas_por_aluno = {}
proposicoes_respostas = {}

for index, row in df_ufsc.iterrows():#para cada linha, ele me da todas as colunas
    if row["CPF"] == "next":
        continue
    cpf = row["CPF"]
    nome = row["aluno"]

    proposicoes_respostas[cpf] = {"nome":nome} 
    proposicoes_respostas[cpf]["respostas_do_aluno"] = {}

    respostas_brutas_por_aluno[cpf] = {"nome":nome}
    respostas_brutas_por_aluno[cpf]["respostas_do_aluno"] = {}

    for questao in range(1,41): #as questoes vão de 1 a 40
        questao = str(questao)
        resposta = (row[questao])
        print(isinstance(resposta,str),resposta)
        if isinstance(resposta,str):
            if resposta== "0" or resposta=="-" or resposta=="--":
                resposta = 0
            elif resposta[0] == "0" and len(resposta)>1:
                resposta = resposta[1::]
                resposta = int(resposta)
            else:
                resposta = int(resposta)
        alternativas_assinaladas = int((bin(resposta)[2:]).count("1"))
        proposicoes_respostas[cpf]["respostas_do_aluno"][questao] = alternativas_assinaladas
        respostas_brutas_por_aluno[cpf]["respostas_do_aluno"][questao] = resposta

with open('./output/json/proposicoes_assinaladas_ufsc.json', 'w') as f:
    json.dump(proposicoes_respostas, f, indent=4, default=str)

with open('./output/json/respostas_brutas_ufsc.json', 'w') as f:
    json.dump(respostas_brutas_por_aluno, f, indent=4, default=str)