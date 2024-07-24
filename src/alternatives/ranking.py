import pandas as pd
import json
ranking_alunos = {}
planilhabruta = './assets/spreadsheets/dados_bruto.csv' #variavel de ambienteglobal df
df = pd.read_csv(planilhabruta)

def corrigir():
    df = pd.read_csv(planilhabruta)
    linhas = df.shape[0]
    colunas = df.shape[1]
    #Para cada linha, vamos percorrer as colunas 
    for linha in range(3,linhas):
        aluno = df.iloc[linha,1]
        aluno_status = {
        'total_acertos': 0,
        'matematica':0,
        "portugues":0,
        "quimica":0,
        "historia":0,
        "geografia":0,
        "fisica":0,
        "biologia":0,
        "filosofia-sociologia":0
    }
        for coluna in range(52,colunas): #A partir da coluna 52 temos os acertos em binario
            valor_binario = df.iloc[linha,coluna]
            #verificando se o aluno acertou a questão
            if valor_binario=="1":
                aluno_status['total_acertos']+=1
                disciplina = df.iloc[2,coluna]
                aluno_status[disciplina]+=1
                
        ranking_alunos[aluno] = aluno_status
    ranking_alunos_ordenado = dict(sorted(ranking_alunos.items(), key=lambda item: item[1]['total_acertos'], reverse=True))
    
    df = pd.DataFrame.from_dict(ranking_alunos_ordenado, orient='index')

    df['cpf'] = list(ranking_alunos_ordenado.keys())[0::]

    # Reordenar as colunas
    df = df[['cpf', 'total_acertos', 'matematica', 'portugues', 'quimica', 'historia', 'geografia', 'fisica', 'biologia', 'filosofia-sociologia']]

    # Salvar o DataFrame em um arquivo CSV
    df.to_csv('./output/spreadsheets/ranking_alunos.xlsx', index=False)
    
    with open('./output/json/ranking_alunos.json', 'w') as f:
        json.dump(ranking_alunos, f, indent=4, default=str)
corrigir()