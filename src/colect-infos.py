import pandas as pd

infos = './assets/spreadsheets/alunos_infos.csv'
df_infos = pd.read_csv(infos,dtype={'CPF': str})
linhas = df_infos.shape[0]

#dicionario cpf:nome
alunos_infos = {}
def generate_info():
    for l in range(linhas):
        cpf = df_infos.iloc[l,1].replace('-','').replace('.','').replace(' ','').replace("'","")
        alunos_infos[cpf] = df_infos.iloc[l,0]

