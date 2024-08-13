import json
import pandas as pd

def calcular_ranking(json_path):
    total_por_disciplina = {}
    with open(json_path, 'r',encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    print(dados)
    for estudante in dados:
        nome = dados[estudante]["nome"]
        total_por_disciplina[estudante] = {"nome":nome}
        total_por_disciplina[estudante]["pontuacão_total"] = {}
        notas = dados[estudante]["parcial_aluno"]
        total_de_acertos_prova = 0
        for materia in notas:
            total = 0
            boletim_materia = notas[materia]
            for pergunta in boletim_materia:
                total_de_pergunta = len(boletim_materia)
                total = boletim_materia[pergunta] + total
                if boletim_materia[pergunta] > 0:
                    total_de_acertos_prova = boletim_materia[pergunta] + total_de_acertos_prova
            total_por_disciplina[estudante]["pontuacão_total"][materia] = f"{round(total,2)}/{total_de_pergunta}" 
        
        total_por_disciplina[estudante]["pontuacão_total"]["total_prova"] = f"{round(total_de_acertos_prova,2)}/40" #total de questoes da ufsc

    dados_ordenados = sorted(total_por_disciplina.items(), key=lambda x: float(x[1]['pontuacão_total']['total_prova'].split('/')[0]), reverse=True)

    with open('./output/json/total por disciplina ufsc.json', 'w', encoding="utf-8") as f:
        json.dump(total_por_disciplina, f, indent=4, default=str, ensure_ascii=False)
    data_list = []
    for key, value in total_por_disciplina.items():
        record = {'CPF': key, 'Nome': value['nome']}
        record.update(value['pontuacão_total'])
        data_list.append(record)

    df = pd.DataFrame(data_list)

    # Salvar o DataFrame em uma planilha Excel
    df.to_csv('./output/spreadsheets/ranking_de_notas.csv', index=False)
    
json_path = "./output/json/parcias_ufsc.json"
calcular_ranking(json_path)    