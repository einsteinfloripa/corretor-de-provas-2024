import json
import pandas as pd
from time import sleep

from ..utils import convert_to_int

def calcular_parciais_ufsc():
    json_path = "./output/json/proposicoes_assinaladas_ufsc.json"
    gabarito_path = "./assets/spreadsheets/Vale - gabarito simufsc I 2024 - Página1.csv"
    parcial_questoes = {}
    gabarito_df = pd.read_csv(gabarito_path)

    with open(json_path, 'r') as arquivo:
        dados = json.load(arquivo)

    def aluno_props_lista(resposta_binario, props_correta):
        respostas = []
        for resposta in range(len(props_correta)):
            props_correta[resposta] = convert_to_int(props_correta[resposta])

        #TO DO: ARRUMAR ESSA LOGICA
        for numero in range(-1,-1*(len(resposta_binario))-1,-1):
            if resposta_binario[numero]=="1":
                valor = 2**((numero*-1)-1)
                respostas.append(valor)
        incorretas = 0
        print("respostas do aluno:",respostas)
        print("proposições corretas: ",props_correta)
        for resposta in respostas:
            print(f"resposta atual: {resposta} condicao: {resposta not in props_correta}")
            if resposta not in props_correta:
                incorretas+=1
        print("proposicoes incorretas consideradas pelo aluno",incorretas)
        print()
        return incorretas

    for estudante in dados:
        estudante_respostas = dados[estudante]["respostas_do_aluno"]
        estudante_nome = dados[estudante]["nome"]
        parcial_questoes[estudante] = {
            "nome":estudante_nome,
            "parcial_aluno":{} 
        }

        for index,row in gabarito_df.iterrows():
            index_string = str(index+1) #index comeca em 0, então tem que somar 1
            lista_de_props_corretas = row["Lista de corretas"].replace(" ", "").split(",")
            disciplina = row["Disciplina"]
            total_de_proposições = row["Total de proposições"]
            proposições_corretas = row["Proposições corretas"]
            aluno_props_binario = estudante_respostas[index_string]
            aluno_total_props = int(aluno_props_binario.count("1"))
            npi = aluno_props_lista(aluno_props_binario,lista_de_props_corretas)
            #print(f"aluno_total_props: {aluno_total_props},npi: {npi}")
            if aluno_total_props > npi:
                pontuacao_questao = ((total_de_proposições - (proposições_corretas - (aluno_total_props - npi)))/total_de_proposições)
            else:
                pontuacao_questao = 0
            parcial_questoes[estudante]["parcial_aluno"][index_string] = round(pontuacao_questao,2)

    with open('./output/json/parcias_ufsc.json', 'w') as f:
        json.dump(parcial_questoes, f, indent=4, default=str)
    

"""
parciais feitas de acordo com o edital da prova do vestibular da ufsc de 2023
https://vestibularunificado2024.ufsc.br/files/2023/10/Edital-Vestibular-2024-RETIFICADO.pdf
"""
