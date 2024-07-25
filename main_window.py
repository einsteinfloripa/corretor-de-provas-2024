import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from src.alternatives.ranking import gerar_ranking
from gui.janelas.simulinho import SimulinhoJanela
from PyQt5.QtGui import QPixmap, QImageReader
from PyQt5.QtCore import Qt
from gui.janelas.utiils import configurar_label_com_imagem

    

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #154163;") 
        self.topo = 200
        self.lado = 550
        self.largura = 800
        self.altura = 600
        self.titulo = "Corretor de Simulados"

        botaoSimulinho = QPushButton("Simulinho", self)
        botaoSimulinho.move(290,150) #posicao do botao = x,y
        botaoSimulinho.resize(200,60) #largura, altura
        botaoSimulinho.setStyleSheet('''
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
        botaoSimulinho.clicked.connect(self.abrir_simulinho)

        botaoEnem = QPushButton("Enem", self)
        botaoEnem.move(290,220) #posicao do botao = x,y
        botaoEnem.resize(200,60) #largura, altura
        botaoEnem.setStyleSheet('''
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

        botaoUfsc = QPushButton("Ufsc", self)
        botaoUfsc.move(290,290) #posicao do botao = x,y
        botaoUfsc.resize(200,60) #largura, altura
        botaoUfsc.setStyleSheet('''
            QPushButton {
                background-color: #00422b;
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

        botaoUdesc = QPushButton("Udesc", self)
        botaoUdesc.move(290,360) #posicao do botao = x,y
        botaoUdesc.resize(200,60) #largura, altura
        botaoUdesc.setStyleSheet('''
            QPushButton {
                background-color: #924800;
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

        botaoPs = QPushButton("Ps", self)
        botaoPs.move(290,430) #posicao do botao = x,y
        botaoPs.resize(200,60) #largura, altura
        botaoPs.setStyleSheet('''
            QPushButton {
                background-color: #121e27;
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

        tituloTopo = QLabel(self)
        tituloTopo.setText("Corretor de simulados")
        tituloTopo.setGeometry(233, 20, 450, 100)  # Ajusta o tamanho e a posição do QLabel
        tituloTopo.setStyleSheet('''
            QLabel {
                font-family: "Cyrillic";   
                font-size: 32px;      
                background-color: transparent;
            }
        ''')

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def abrir_simulinho(self):
        self.simulinhoJanela = SimulinhoJanela()
        self.simulinhoJanela.show()

aplicacao = QApplication(sys.argv)

j = Janela()
sys.exit(aplicacao.exec_())