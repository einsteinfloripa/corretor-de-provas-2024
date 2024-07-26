from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PyQt5 import QtGui
from .utiils import configurar_label_com_imagem, botaoGerarVariaveisStyle, botaoGerarResultadosStyle, tituloTopoStyle, SelecionarDadosBrutosStyle, SelecionarInformaçõesStyle, SelecionarCaminhoStyle
class SimulinhoJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #362500;") 
        self.topo = 200
        self.lado = 550
        self.largura = 800
        self.altura = 600
        self.titulo = "Corretor de Simulados"

        botaoGerarVariaveis = QPushButton("GerarVariaveis", self)
        botaoGerarVariaveis.move(170,450)
        botaoGerarVariaveis.resize(200,60)
        botaoGerarVariaveis.setStyleSheet(botaoGerarVariaveisStyle)
        #botaoGerarVariaveis.clicked.connect()

        botaoGerarResultados = QPushButton("GerarResultados", self)
        botaoGerarResultados.move(450,450)
        botaoGerarResultados.resize(200,60)
        botaoGerarResultados.setStyleSheet(botaoGerarResultadosStyle)

        tituloTopo = QLabel(self)
        tituloTopo.setText("Simulinho")
        tituloTopo.setGeometry(320, 20, 450, 100)  # x,y,width, height
        tituloTopo.setStyleSheet(tituloTopoStyle)


        self.icon = QLabel(self)
        configurar_label_com_imagem(self.icon, "./assets/icons/einsteinlogo.png", 100, 100, 30, 470)
    

        # Criação do QPushButton
        self.SelecionarDadosBrutos = QPushButton("Selecionar dados brutos", self)
        self.SelecionarDadosBrutos.move(290,150)
        self.SelecionarDadosBrutos.resize(200,65)
        self.SelecionarDadosBrutos.setStyleSheet(SelecionarDadosBrutosStyle)
        self.SelecionarDadosBrutos.clicked.connect(self.open_file_dialog)

        self.SelecionarInformações = QPushButton("Selecionar infos alunos", self)
        self.SelecionarInformações.move(290,250)
        self.SelecionarInformações.resize(200,65)
        self.SelecionarInformações.setStyleSheet(SelecionarInformaçõesStyle)
        self.SelecionarInformações.clicked.connect(self.open_file_dialog)

        self.SelecionarCaminho = QPushButton("Caminho dos arquivos", self)
        self.SelecionarCaminho.move(290,350)
        self.SelecionarCaminho.resize(200,65)
        self.SelecionarCaminho.setStyleSheet(SelecionarCaminhoStyle)
        self.SelecionarCaminho.clicked.connect(self.open_file_dialog)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "", "Todos os Arquivos (*);;Arquivos de Texto (*.txt)", options=options)
        # Obtém o botão que enviou o sinal
        button = self.sender()
        print(file_name)
        if file_name:
            button.setText(f"Arquivo selecionado: {file_name}")
        else:
            self.SelecionarDadosBrutos.setText("Nenhum arquivo selecionado")


