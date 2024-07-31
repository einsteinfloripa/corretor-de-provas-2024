import pandas as pd
import json
from time import sleep
df_ufsc = pd.read_csv("./assets/spreadsheets/Cópia de SimuUFSC 2024 - Dados brutos.xlsx - Sheet1.csv")
total_de_linhas = df_ufsc.shape[0]

respostas = {}

for index, row in df_ufsc.iterrows():#para cada linha, ele me da todas as colunas
    if row["CPF"] == "next":
        continue
    cpf = row["CPF"]
    nome = row["aluno"]
    respostas[cpf] = {"nome":nome} 

    respostas[cpf]["respostas_do_aluno"] = {}
    for questao in range(1,41): #as questoes vão de 1 a 40
        questao = str(questao)
        resposta = (row[questao])
        respostas[cpf]["respostas_do_aluno"][questao] = resposta

with open('./output/json/respostas_ufsc.json', 'w') as f:
        json.dump(respostas, f, indent=4, default=str)