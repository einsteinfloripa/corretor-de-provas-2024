from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PyQt5 import QtGui
from .utiils import configurar_label_com_imagem, botaoGerarResultadosStyle, tituloTopoStyle, SelecionarDadosBrutosUfscStyle, SelecionarCaminhoUfscStyle, SelecionarCaminhoUfscStyle, SelecionarValeUfscGabaritoStyle, SelecionarInformaçõesUfscStyle
from src.alternatives.alternatives import gerar_grafico_distruibuicao

class UfscJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #00422b;") 
        self.topo = 200
        self.lado = 550
        self.largura = 800
        self.altura = 600
        self.titulo = "Corretor da UFSC"
        self.CaminhosDeArquivos = {
            "dados_brutos" : "",
            "infos_alunos":"",
            "salvar_arquivos":""
        }
        # botaoGerarVariaveis = QPushButton("GerarVariaveis", self)
        # botaoGerarVariaveis.move(170,450)
        # botaoGerarVariaveis.resize(200,60)
        # botaoGerarVariaveis.setStyleSheet(botaoGerarResultadosStyle)
        # botaoGerarVariaveis.clicked.connect(lambda:gerar_grafico_distruibuicao("simulinho",self.CaminhosDeArquivos["dados_brutos"],self.CaminhosDeArquivos["salvar_arquivos"]))
        # botaoGerarVariaveis.clicked.connect(self.textoDeStatus)

        botaoGerarResultados = QPushButton("GerarResultados", self)
        botaoGerarResultados.move(450,450)
        botaoGerarResultados.resize(200,60)
        botaoGerarResultados.setStyleSheet(botaoGerarResultadosStyle)

        tituloTopo = QLabel(self)
        tituloTopo.setText("UFSC")
        tituloTopo.setGeometry(350, 20, 450, 100)  # x,y,width, height
        tituloTopo.setStyleSheet(tituloTopoStyle)


        self.icon = QLabel(self)
        configurar_label_com_imagem(self.icon, "./assets/icons/einsteinlogo.png", 100, 100, 30, 470)
    

        # Criação do QPushButton
        self.SelecionarDadosBrutos = QPushButton("Selecionar dados brutos", self)
        self.SelecionarDadosBrutos.setObjectName("dados_brutos")
        self.SelecionarDadosBrutos.move(290,150)
        self.SelecionarDadosBrutos.resize(200,65)
        self.SelecionarDadosBrutos.setStyleSheet(SelecionarDadosBrutosUfscStyle)
        self.SelecionarDadosBrutos.clicked.connect(self.open_file_dialog)

        self.SelecionarInformações = QPushButton("Selecionar infos alunos", self)
        self.SelecionarInformações.setObjectName("infos_alunos")
        self.SelecionarInformações.move(290,250)
        self.SelecionarInformações.resize(200,65)
        self.SelecionarInformações.setStyleSheet(SelecionarInformaçõesUfscStyle)
        self.SelecionarInformações.clicked.connect(self.open_file_dialog)

        self.SelecionarInformações = QPushButton("Selecionar gabarito vale", self)
        self.SelecionarInformações.setObjectName("Gabarito vale")
        self.SelecionarInformações.move(290,250)
        self.SelecionarInformações.resize(200,65)
        self.SelecionarInformações.setStyleSheet(SelecionarValeUfscGabaritoStyle)
        self.SelecionarInformações.clicked.connect(self.open_file_dialog)

        self.SelecionarCaminho = QPushButton("Caminho dos arquivos", self)
        self.SelecionarCaminho.setObjectName("salvar_arquivos")
        self.SelecionarCaminho.move(290,350)
        self.SelecionarCaminho.resize(200,65)
        self.SelecionarCaminho.setStyleSheet(SelecionarCaminhoUfscStyle)
        self.SelecionarCaminho.clicked.connect(self.openDirectory)

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
            self.CaminhosDeArquivos[button.objectName()] = file_name
            button.setText(f"Arquivo selecionado: {file_name}")
            print(self.CaminhosDeArquivos)
        else:
            self.SelecionarDadosBrutos.setText("Nenhum arquivo selecionado")
    
    def openDirectory(self):
        options = QFileDialog.Options()
        folder = QFileDialog.getExistingDirectory(self, "Selecione o Diretório", "", options=options)
        button = self.sender()
        if folder:
            self.CaminhosDeArquivos[button.objectName()] = folder
            button.setText(f"Arquivo selecionado: {folder}")
            print(f"Diretório selecionado: {folder}")
            # Aqui você pode adicionar lógica para salvar o caminho selecionado para uso futuro

    
    def textoDeStatus(self):
        textoDeStatus = QLabel(self)
        textoDeStatus.setText("Variaveis Criadas!")
        textoDeStatus.setGeometry(220, 450, 450, 100)  # x,y,width, height
        textoDeStatus.setStyleSheet(tituloTopoStyle)


