import pandas as pd

infos = './assets/spreadsheets/alunos_infos_2024.csv'
df_infos = pd.read_csv(infos,dtype={'CPF': str})
linhas = df_infos.shape[0]

#dicionario cpf:nome
alunos_infos = {}
for index, row in df_infos.iterrows():
    cpf = row["CPF"].replace('-','').replace('.','').replace(' ','').replace("'","")
    alunos_infos[cpf] = row["Nome Completo"]

def printDict():
    for aluno in alunos_infos:
        print(aluno,':',alunos_infos[aluno])
