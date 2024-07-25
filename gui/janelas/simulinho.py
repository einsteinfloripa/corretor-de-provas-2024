from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import QtGui
from .utiils import configurar_label_com_imagem, botaoGerarVariaveisStyle, botaoGerarResultadosStyle, tituloTopoStyle
class SimulinhoJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #154163;") 
        self.topo = 200
        self.lado = 550
        self.largura = 800
        self.altura = 600
        self.titulo = "Corretor de Simulados"

        botaoGerarVariaveis = QPushButton("GerarVariaveis", self)
        botaoGerarVariaveis.move(170,450)
        botaoGerarVariaveis.resize(200,60)
        botaoGerarVariaveis.setStyleSheet(botaoGerarVariaveisStyle)

        botaoGerarResultados = QPushButton("GerarResultados", self)
        botaoGerarResultados.move(450,450)
        botaoGerarResultados.resize(200,60)
        botaoGerarResultados.setStyleSheet(botaoGerarResultadosStyle)

        tituloTopo = QLabel(self)
        tituloTopo.setText("Simulinho")
        tituloTopo.setGeometry(320, 20, 450, 100)  # Ajusta o tamanho e a posição do QLabel. Pode ser usado o resize tambem
        tituloTopo.setStyleSheet(tituloTopoStyle)


        self.icon = QLabel(self)
        configurar_label_com_imagem(self.icon, "./assets/icons/einsteinlogo.png", 100, 100, 30, 470)
    
        self.CarregarJanela()


    def CarregarJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
