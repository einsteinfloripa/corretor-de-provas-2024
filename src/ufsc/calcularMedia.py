import json
def calcular_media_acertos(json_path):
    with open(json_path, 'r') as arquivo:
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
    
    medias_acertos["Media de acertos"] = media_prova
    

    with open('./output/json/media_disciplinas_ufsc.json', 'w', encoding='utf-8') as f:
        json.dump(medias_acertos, f, indent=4, default=str, ensure_ascii=False)

calcular_media_acertos("./output/json/parcias_ufsc.json")