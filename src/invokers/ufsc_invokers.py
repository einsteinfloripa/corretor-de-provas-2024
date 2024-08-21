from ..ufsc.organizarRespostas import generate_json_ufsc

from ..ufsc.calcularParcial import calcular_parciais_ufsc

from ..ufsc.calcularMedia import calcular_media_acertos

from ..ufsc.ranking import calcular_ranking

from ..ufsc.pdfIndividual import gerar_relatorios_individuais


def main(dados_brutos_path, ):
    generate_json_ufsc()
    calcular_parciais_ufsc()
    calcular_media_acertos("./output/json/parcias_ufsc.json")
    calcular_ranking("./output/json/parcias_ufsc.json")
    gerar_relatorios_individuais()

if __name__ == "__main__":
    main()