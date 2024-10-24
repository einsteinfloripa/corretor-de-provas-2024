import json
import pandas as pd
def calcular_media_acertos(json_path, main_output_path):
    print("------------------------------------------------------------------------")
    print("Calculando média de acertos de cada disciplina...")
    with open(json_path, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    # Inicializar um dicionário para armazenar a soma das notas e a quantidade de alunos por disciplina
    soma_acertos = {}
    
    # Iterar sobre cada aluno
    for aluno_cpf, aluno_dados in dados.items():
        disciplinas = aluno_dados["parcial_aluno"]

        for disciplina, notas in disciplinas.items():
            if disciplina not in soma_acertos:
                soma_acertos[disciplina] = 0
                
            
            # Somar os acertos da disciplina para o aluno atual
            soma_acertos[disciplina] += sum(notas.values())
    qtd_alunos = len(dados)
    
    #Calcular a média de acertos para cada disciplina
    medias_acertos = {}
    media_prova = 0
    for disciplina in soma_acertos:
        media_prova = round(((soma_acertos[disciplina] / qtd_alunos) + media_prova),2)
        medias_acertos[disciplina] = f"{round(soma_acertos[disciplina] / qtd_alunos,2)}/{len(disciplinas[disciplina])}"
    
    medias_acertos["Media de acertos"] = f"{(str(media_prova))}/40"
    

    with open(f'{main_output_path}/media_disciplinas_ufsc.json', 'w', encoding='utf-8') as f:
        json.dump(medias_acertos, f, indent=4, default=str, ensure_ascii=False)
    
    df = pd.DataFrame(list(medias_acertos.items()), columns=['Matéria', 'Resultado médio de acertos'])
    df.to_csv(f"{main_output_path}/media_disciplinas_ufsc.csv", index=False)
    print("Média de acertos calculadas com sucesso!!")
    print("------------------------------------------------------------------------")
    print()
    print()

if __name__ == "__main__":
    calcular_media_acertos("./output/json/parcias_ufsc.json","./output/json" )