import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from src.alternatives.ranking import gerar_ranking
from gui.janelas.simulinho import SimulinhoJanela
from gui.janelas.ufsc import UfscJanela
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from gui.janelas.utiils import configurar_label_com_imagem, EnemBotaoStyle, UfscBotaoStyle, SimulinhoBotaoStyle, UdescBotaoStyle, PsBotaoStyle, tituloTopoStyle, como_usar_link_style, como_usar_link, versão_style

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #154374;")
        self.topo = 200
        self.lado = 550
        self.largura = 800
        self.altura = 600
        self.titulo = "Corretor de Simulados"
        botaoSimulinho = QPushButton("Simulinho", self)
        botaoSimulinho.move(290, 150)  # posição do botão = x,y
        botaoSimulinho.resize(200, 60)  # largura, altura
        botaoSimulinho.setStyleSheet(SimulinhoBotaoStyle)
        botaoSimulinho.clicked.connect(self.abrir_simulinho)

        botaoEnem = QPushButton("Enem", self)
        botaoEnem.move(290, 220)
        botaoEnem.resize(200, 60)
        botaoEnem.setStyleSheet(EnemBotaoStyle)

        botaoUfsc = QPushButton("Ufsc", self)
        botaoUfsc.move(290, 290)
        botaoUfsc.resize(200, 60)
        botaoUfsc.setStyleSheet(UfscBotaoStyle)
        botaoUfsc.clicked.connect(self.abrir_ufsc)

        botaoUdesc = QPushButton("Udesc", self)
        botaoUdesc.move(290, 360)
        botaoUdesc.resize(200, 60)
        botaoUdesc.setStyleSheet(UdescBotaoStyle)

        botaoPs = QPushButton("Ps", self)
        botaoPs.move(290, 430)
        botaoPs.resize(200, 60)
        botaoPs.setStyleSheet(PsBotaoStyle)

        tituloTopo = QLabel(self)
        tituloTopo.setText("Corretor de simulados")
        tituloTopo.setGeometry(233, 20, 450, 100)  # Ajusta o tamanho e a posição do QLabel
        tituloTopo.setStyleSheet(tituloTopoStyle)

        versao = QLabel(self)
        versao.setText("versão 24.1.0")
        versao.setGeometry(690, 540, 100, 50)  # Ajusta o tamanho e a posição do QLabel
        versao.setStyleSheet(versão_style)

        comoUsar = QLabel(self)
        como_usar_texto = f'''
            <a href="{como_usar_link}" style="color: #e5e5e5; font-family: 'Cyrillic'; font-size: 20px;">
                {"Documentação"}
            </a>
        '''

        comoUsar.setText(como_usar_texto)
        comoUsar.setGeometry(315, 550, 135, 30)  # Ajusta o tamanho e a posição do QLabel
        comoUsar.setStyleSheet(como_usar_link_style)
        comoUsar.setOpenExternalLinks(True)  # Permite que links abram no navegador padrão

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
