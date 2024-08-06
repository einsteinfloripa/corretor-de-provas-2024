import json
import pandas as pd


from ..utils import convert_to_int

converter_texto = {
    "InglÃªs": "Inglês",
    "Ingles": "Inglês",
    "Espanhol":"Espanhol"
}
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
        for resposta in respostas:
            if resposta not in props_correta:
                incorretas+=1
        return incorretas

    for estudante in dados:
        estudante_respostas = dados[estudante]["respostas_do_aluno"]
        estudante_nome = dados[estudante]["nome"]
        parcial_questoes[estudante] = {
            "nome":estudante_nome,
            "parcial_aluno":{
                "Português/Literatura":{},
                "Matemática":{},
                "Biologia":{},
                "História":{},
                "Geografia":{},
                "Filosofia/Sociologia":{},
                "Física":{},
                "Química":{},
                "linguagens":{}
            } 
        }
        pontos_disciplina = {}

        for index,row in gabarito_df.iterrows():
            index_string = str(index+1) #index comeca em 0, então tem que somar 1
            lista_de_props_corretas = row["Lista de corretas"].replace(" ", "").split(",")
            disciplina = row["Disciplina"]
            
            total_de_proposições = row["Total de proposições"]
            proposições_corretas = row["Proposições corretas"]
            
            if disciplina == "Inglês":
                linguagem = dados[estudante]["lingua"]
                linguagem = converter_texto[linguagem]
                if linguagem == "Espanhol":
                    total_de_proposições = row["Total de proposições espanhol"]
                    proposições_corretas = row["Proposições corretas espanhol"]
            aluno_props_binario = estudante_respostas[index_string]
            aluno_total_props = int(aluno_props_binario.count("1"))
            npi = aluno_props_lista(aluno_props_binario,lista_de_props_corretas)
            if aluno_total_props > npi:
                pontuacao_questao = ((total_de_proposições - (proposições_corretas - (aluno_total_props - npi)))/total_de_proposições)
            else:
                pontuacao_questao = 0
            if disciplina=="Inglês" or disciplina=="Espanhol":
                disciplina = "linguagens"
            parcial_questoes[estudante]["parcial_aluno"][disciplina][index_string] = round(pontuacao_questao,2)

    with open('./output/json/parcias_ufsc.json', 'w', encoding="utf-8") as f:
        json.dump(parcial_questoes, f, indent=4, default=str, ensure_ascii=False)
    

"""
parciais feitas de acordo com o edital da prova do vestibular da ufsc de 2023
https://vestibularunificado2024.ufsc.br/files/2023/10/Edital-Vestibular-2024-RETIFICADO.pdf
"""
