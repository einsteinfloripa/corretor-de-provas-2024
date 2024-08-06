import pandas as pd
import json
from ..utils import convert_to_int
def generate_json_ufsc():
    df_ufsc = pd.read_csv("./assets/spreadsheets/Cópia de SimuUFSC 2024 - Dados brutos.xlsx - Sheet1.csv", encoding='utf-8')
    total_de_linhas = df_ufsc.shape[0]

    respostas_brutas_por_aluno = {}
    proposicoes_respostas = {}


    for index, row in df_ufsc.iterrows():#para cada linha, ele me da todas as colunas
        if row["CPF"] == "next":
            continue
        cpf = row["CPF"]
        nome = row["aluno"]
        lingua = row["línguas"]
        proposicoes_respostas[cpf] = {"nome":nome, "lingua":lingua} 
        proposicoes_respostas[cpf]["respostas_do_aluno"] = {}

        respostas_brutas_por_aluno[cpf] = {"nome":nome, "lingua":lingua}
        respostas_brutas_por_aluno[cpf]["respostas_do_aluno"] = {}

        for questao in range(1,41): #as questoes vão de 1 a 40
            questao = str(questao)
            resposta = (row[questao])
            
            resposta = convert_to_int(resposta)
            alternativas_assinaladas = bin(resposta)[2:]
            proposicoes_respostas[cpf]["respostas_do_aluno"][questao] = alternativas_assinaladas
            respostas_brutas_por_aluno[cpf]["respostas_do_aluno"][questao] = resposta

    with open('./output/json/proposicoes_assinaladas_ufsc.json', 'w',encoding='utf-8') as f:
        json.dump(proposicoes_respostas, f, indent=4, default=str, ensure_ascii=False)

    with open('./output/json/respostas_brutas_ufsc.json', 'w', encoding='utf-8') as f:
        json.dump(respostas_brutas_por_aluno, f, indent=4, default=str, ensure_ascii=False)