import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from src.alternatives.ranking import gerar_ranking
from gui.janelas.simulinho import SimulinhoJanela
from PyQt5.QtGui import QPixmap, QImageReader
from PyQt5.QtCore import Qt
from gui.janelas.utiils import configurar_label_com_imagem, EnemBotaoStyle, UfscBotaoStyle, SimulinhoBotaoStyle, UdescBotaoStyle, PsBotaoStyle, tituloTopoStyle

    

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
        botaoSimulinho.setStyleSheet(SimulinhoBotaoStyle)
        botaoSimulinho.clicked.connect(self.abrir_simulinho)

        botaoEnem = QPushButton("Enem", self)
        botaoEnem.move(290,220) #posicao do botao = x,y
        botaoEnem.resize(200,60) #largura, altura
        botaoEnem.setStyleSheet(EnemBotaoStyle)

        botaoUfsc = QPushButton("Ufsc", self)
        botaoUfsc.move(290,290) #posicao do botao = x,y
        botaoUfsc.resize(200,60) #largura, altura
        botaoUfsc.setStyleSheet(UfscBotaoStyle)

        botaoUdesc = QPushButton("Udesc", self)
        botaoUdesc.move(290,360) #posicao do botao = x,y
        botaoUdesc.resize(200,60) #largura, altura
        botaoUdesc.setStyleSheet(UdescBotaoStyle)

        botaoPs = QPushButton("Ps", self)
        botaoPs.move(290,430) #posicao do botao = x,y
        botaoPs.resize(200,60) #largura, altura
        botaoPs.setStyleSheet(PsBotaoStyle)

        tituloTopo = QLabel(self)
        tituloTopo.setText("Corretor de simulados")
        tituloTopo.setGeometry(233, 20, 450, 100)  # Ajusta o tamanho e a posição do QLabel
        tituloTopo.setStyleSheet(tituloTopoStyle)

        self.icon = QLabel(self)
        configurar_label_com_imagem(self.icon, "./assets/icons/einsteinlogo.png", 100, 100, 30, 470)
        
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