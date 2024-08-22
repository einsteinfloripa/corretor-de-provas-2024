import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Função para criar um relatório PDF


# with open(f"{main_path}/media_disciplinas_ufsc.json", 'r') as arquivo:
#     media_geral = json.load(arquivo)

def create_report(data, filename):
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []
    
    # Título
    
    # Dados do Aluno
    student_info = [
        ["Nome", data['name']],
        ["CPF", data['cpf']],
        ["Linguagem",data["idioma_aluno"]]
    ]
    
    table = Table(student_info, colWidths=[100, 400])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Desempenho por Matéria
    estilo = styles['Heading2']
    estilo.alignment = 1
    elements.append(Paragraph("Desempenho por Matéria", estilo))
    subject_data = [["Matéria", "Totais de acerto: ", "Média geral"]] + data['subjects']
    
    table = Table(subject_data, colWidths=[100, 200, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Resultado por questão
    question_results = [["Questão", "Gabarito", "Você", "Parcial"]] + data['questions']
    
    # Ajustando a largura das colunas
    colWidths = [50, 50, 50, 50]  # Atualize a largura das colunas se necessário
    
    table = Table(question_results, colWidths=colWidths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Salvar PDF
    pdf.build(elements)

# Dados de exemplo
"""data = {
    'name': 'Sofia Silveira Yukimura Lopez',
    'cpf': '111.177.339-47',
    'objective_score': 29,
    'subjects': [
        ["Matemática", "2", "4,61"],
        ["Física", "4", "3,17"],
        ["Química", "4", "2,89"],
        ["Biologia", "3", "3,81"],
        ["Geografia", "2", "2,47"],
        ["História", "4", "2,32"],
        ["Literatura", "4", "3,30"],
        ["Português", "6", "4,96"],
        ["Total", '29', media_geral["Media de acertos"]]
    ],
    'questions': [
        ["1", "A", "D", "0"],  # Adicione a pontuação obtida para cada questão
        ["2", "ANULADA", "E", "0"],
        ["3", "D", "C", "0"],
        ["4", "C", "D", "0"],
        ["5", "C", "B", "0"],
        ["6", "D", "B", "0"],
        ["7", "ANULADA", "C", "0"],
        ["8", "C", "D", "0"],
        ["9", "C", "", "0"],
        ["10", "A", "B", "0"],
        ["11", "B", "D", "0"],
        ["12", "C", "", "0"],
        ["13", "D", "B", "0"],
        ["14", "D", "E", "0"],
        ["15", "C", "C", "1"],
        ["16", "C", "C", "1"],
        ["17", "E", "E", "1"],
        ["18", "B", "D", "0"],
        ["19", "C", "D", "0"],
        ["20", "A", "A", "1"],
        ["21", "E", "C", "0"],
        ["22", "C", "C", "1"],
        ["23", "E", "E", "1"],
        ["24", "C", "C", "1"],
        ["25", "B", "A", "0"],
        ["26", "A", "A", "1"],
        ["27", "C", "B", "0"],
        ["28", "C", "B", "0"],
        ["29", "D", "D", "1"],
        ["30", "C", "C", "1"],
        ["31", "C", "B", "0"],
        ["32", "D", "D", "1"],
        ["33", "ANULADA", "C", "0"],
        ["34", "C", "D", "0"],
        ["35", "D", "D", "1"],
        ["36", "B", "C", "0"],
        ["37", "D", "B", "0"],
        ["38", "D", "B", "0"],
        ["39", "D", "C", "0"],
        ["40", "C", "C", "1"]
    ]
}"""