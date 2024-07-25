import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from src.alternatives.ranking import gerar_ranking


class SimulinhoJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #154163;") 
        self.topo = 200
        self.lado = 550
        self.largura = 800
        self.altura = 800
        self.titulo = "Corretor de Simulados"

        botaoGerarVariaveis = QPushButton("GerarVariaveis", self)
        botaoGerarVariaveis.move(250,150) #posicao do botao = x,y
        botaoGerarVariaveis.resize(300,100) #largura, altura
        botaoGerarVariaveis.setStyleSheet('''
            QPushButton {
                background-color: #362500;
                border-radius: 6px;
                color: #e7e6e3;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #5a4d3d;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        ''')
        #botaoGerarVariaveis.clicked.connect(self.Simulinho)

        botaoGerarResultados = QPushButton("GerarResultados", self)
        botaoGerarResultados.move(250,280) #posicao do botao = x,y
        botaoGerarResultados.resize(300,100) #largura, altura
        botaoGerarResultados.setStyleSheet('''
            QPushButton {
                background-color: #493b72;
                border-radius: 6px;
                color: #e7e6e3;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #5a4d3d;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        ''')


    def CarregarJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


simulinho = SimulinhoJanela()
sys.exit(aplicacao.exec_())
