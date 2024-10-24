import json
import pandas as pd

from ..utils import convert_to_int

converter_texto = {
    "InglÃªs": "Inglês",
    "Ingles": "Inglês",
    "Espanhol":"Espanhol"
}
def calcular_parciais_ufsc(main_path,gabarito_vale):
    print("------------------------------------------------------------------------")
    print("Calculando parciais de acordo com o edital da UFSC...")
    json_path = f"{main_path}/proposicoes_assinaladas_ufsc.json"
    parcial_questoes = {}
    gabarito_df = pd.read_csv(gabarito_vale,dtype={"Total de proposições": int}, encoding='utf-8')
    gabarito_df['Total de proposições'] = gabarito_df['Total de proposições'].astype(int)

    with open(json_path, 'r') as arquivo:
        dados = json.load(arquivo)

    def aluno_props_lista(resposta_binario, props_correta):#valor em binário, proposições corretas da questão atual
        respostas = [] #lista de proposições assinaladas pelo estudante
        for resposta in range(len(props_correta)):
            props_correta[resposta] = convert_to_int(props_correta[resposta])

        #TO DO: ARRUMAR ESSA LOGICA
        for numero in range(-1,-1*(len(resposta_binario))-1,-1):
            if resposta_binario[numero]=="1":
                valor = 2**((numero*-1)-1)
                respostas.append(valor)
        incorretas = 0
        corretas = 0
        for resposta in respostas:
            if resposta not in props_correta:
                incorretas+=1
            else:
                corretas+=1
        return incorretas,corretas,respostas
    for estudante in dados:
        estudante_respostas = dados[estudante]["respostas_do_aluno"]
        estudante_nome = dados[estudante]["nome"]
        parcial_questoes[estudante] = {
            "nome":estudante_nome,
            "parcial_aluno":{
            } 
        }

        for index,row in gabarito_df.iterrows():
            index_string = str(index+1) #index comeca em 0, então tem que somar 1
            lista_de_props_corretas = row["Lista de corretas"].replace(" ", "").split(",")
            disciplina = row["Disciplina"]
            ntpc = len(lista_de_props_corretas)
            np = row["Total de proposições"]
            proposições_corretas = row["Proposições corretas"]
            if disciplina == "Inglês":
                linguagem = dados[estudante]["lingua"]
                linguagem = converter_texto[linguagem]
                print("A linguagem do aluno:", linguagem)
                if linguagem == "Espanhol":
                    np = row["Total de proposições espanhol"]
                    proposições_corretas = row["Proposições corretas espanhol"]
            aluno_props_binario = estudante_respostas[index_string]
            aluno_total_props = int(aluno_props_binario.count("1"))
            npi,npc,opcoes_assinaladas_aluno = aluno_props_lista(aluno_props_binario,lista_de_props_corretas)
            if npc > npi:
                pontuacao_questao = ((np - (ntpc - (npc - npi)))/np)
            else:
                pontuacao_questao = 0
            if disciplina=="Inglês" or disciplina=="Espanhol":
                disciplina = "linguagens"
            if disciplina not in parcial_questoes[estudante]["parcial_aluno"]:
                parcial_questoes[estudante]["parcial_aluno"][disciplina] = {index_string:round(pontuacao_questao,2)}
            else:
                parcial_questoes[estudante]["parcial_aluno"][disciplina][index_string] = round(pontuacao_questao,2)
    with open(f'{main_path}/parcias_ufsc.json', 'w', encoding="utf-8") as f:
        json.dump(parcial_questoes, f, indent=4, default=str, ensure_ascii=False)
    print("Parciais da UFSC foram calculadas com sucesso.")
    print("Arquivos gerados com sucesso!!")
    print("------------------------------------------------------------------------")
    print()
    print()

if __name__ == "__main__":
    calcular_parciais_ufsc("./src./output.","./src./assets/spreadsheets./a.csv")
"""
parciais feitas de acordo com o edital da provas do vestibular da ufsc de 2024
https://drive.google.com/file/d/1sUbkCkJ5-XZiPlAB6S72HIkgJC0XoqiX/view?usp=sharing
"""
