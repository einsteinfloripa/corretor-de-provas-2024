import pandas as pd 

df = pd.read_csv("./assets/spreadsheets/dados_bruto.csv" )
print(df.shape[0],df.shape[1])
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from src.utils import textCorrector, textColor, numero_de_colunas
from src.utils import ler_planilha

planilhabruta = './assets/spreadsheets/dados_bruto.csv' #variavel de ambiente
pdf_pages = PdfPages("./output/pdf/Distribuição de Alternativas.pdf")  # Cria um objeto PDF

df = pd.read_csv(planilhabruta)
print(df.shape[0],df.shape[1])
def gerar_grafico_distruibuicao(colunas,n_linhas,prova):
    data_per = {}
    total_de_colunas = numero_de_colunas[prova]
    fig_count = 0
    for coluna in range(2, total_de_colunas):
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        acertaram = 0
        erraram = 0
        print(f"QUESTAO: {coluna-1}")
        for linha in range(3,99g):
            colunaG = coluna - 3
            disciplina = df.iloc[2, coluna]
            gabaritoC = df.iloc[0,coluna]
            resposta_aluno = df.iloc[linha, coluna]
            print(f"aluno: {resposta_aluno} | gabarito: {gabaritoC}")
            if resposta_aluno == 'NAO DETECTADO':
                continue
            if resposta_aluno == "A":
                a += 1
            elif resposta_aluno == "B":
                b += 1
            elif resposta_aluno == "C":
                c += 1
            elif resposta_aluno == 'D':
                d += 1
            elif resposta_aluno == "E":
                e += 1
            if resposta_aluno == gabaritoC:
                acertaram += 1
            else:
                erraram += 1
        print()

        total_respostas = acertaram + erraram
        acertaram = (acertaram / total_respostas) * 100
        erraram = (erraram / total_respostas) * 100
        acertaram = f'{acertaram:.1f}'
        erraram = f'{erraram:.1f}'
        questoes_em_porcentagem = {
            'discplina':disciplina,
            'erros':erraram,
            'acertos':acertaram
        }
        questaoStr = questoes_em_porcentagem
        data_per[f'Questão {questaoStr}'] = coluna
        data = {
            f'A|{a}': a,
            f'B|{b}': b,
            f'C|{c}': c,
            f'D|{d}': d,
            f'E|{e}': e,
        }

        print(f'Questão:{coluna-2} Disciplina:{disciplina} Gabarito: {gabaritoC}\n A: {a}\n B: {b}\n C: {c}\n D: {d}\n E: {e} ')
        print(erraram, acertaram)
        courses = list(data.keys())
        values = list(data.values())
        
        if fig_count == 0:
            fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # Duas figuras por página
            fig_count = 0

        # Criando o gráfico de barras
        # Criando o gráfico de barras
        axs[fig_count].bar(courses, values, color=textColor[disciplina], width=0.4)
        axs[fig_count].set_xlabel(f"Resposta correta: {gabaritoC}", fontsize=11)
        axs[fig_count].set_ylabel(f"Quantidade de vezes assinalada", fontsize=10)
        axs[fig_count].set_title(f"Questão: {coluna-2} Disciplina: {textCorrector[disciplina]}", fontsize=11)
        if gabaritoC != 'Anulada':
            axs[fig_count].text(0.52, 1.06, f" Erraram: {erraram}% | Acertaram: {acertaram}% ", ha='center', transform=axs[fig_count].transAxes, fontsize=11)

        # Definindo a escala do eixo y entre 5 e 80
        axs[fig_count].set_ylim(5, 80)

        
        fig_count += 1
        if fig_count == 2:
            pdf_pages.savefig(fig)
            plt.close(fig)
            fig_count = 0

    if fig_count != 0:
        pdf_pages.savefig(fig)
        plt.close(fig)

    pdf_pages.close()

#createpdf.tableNotes(data_per)
#print(df.iloc[linha,coluna])
print(df.iloc[2,2])
