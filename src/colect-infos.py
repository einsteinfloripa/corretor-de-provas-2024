import pandas as pd

infos = './assets/alunos_infos_2024 - Respostas ao formulário 1.csv'
df_infos = pd.read_csv(infos,dtype={'CPF': str})
linhas = df_infos.shape[0]

#dicionario cpf:nome
alunos_infos = {}
for l in range(linhas):
    cpf = df_infos.iloc[l,1].replace('-','').replace('.','').replace(' ','').replace("'","")
    alunos_infos[cpf] = df_infos.iloc[l,0]

def printDict():
    for aluno in alunos_infos:
        print(aluno,':',alunos_infos[aluno])

