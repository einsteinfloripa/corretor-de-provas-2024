from  src.simulinho.distribuicao import gerar_grafico_distruibuicao
from src.simulinho.ranking import gerar_ranking
def main_simulinho(prova, caminhoDadosBrutos, caminhoSalvarArquivos):
    print("Gerando gráfico de distribuição da prova...")
    gerar_grafico_distruibuicao(prova, caminhoDadosBrutos, caminhoSalvarArquivos),
    print("Gerando ranking de notas...")
    gerar_ranking(caminhoDadosBrutos, caminhoSalvarArquivos)
    print("Ranking Gerado")