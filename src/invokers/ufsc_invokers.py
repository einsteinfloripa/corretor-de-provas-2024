from ..ufsc.organizarRespostas import generate_json_ufsc

from ..ufsc.calcularParcial import calcular_parciais_ufsc

from ..ufsc.calcularMedia import calcular_media_acertos

from ..ufsc.ranking import calcular_ranking

from ..ufsc.pdfIndividual import gerar_relatorios_individuais


def main(dados_brutos_path, main_output_path, gabarito_vale_csv, relatorios_alunos_path, gabarito_vale_convertido):
    generate_json_ufsc(dados_brutos_path, main_output_path)
    calcular_parciais_ufsc(main_output_path, gabarito_vale_csv)
    calcular_media_acertos(f"{main_output_path}/parcias_ufsc.json", main_output_path)
    calcular_ranking(f"{main_output_path}","/parcias_ufsc.json")
    gerar_relatorios_individuais(main_output_path, relatorios_alunos_path, gabarito_vale_convertido)

if __name__ == "__main__":
    main()