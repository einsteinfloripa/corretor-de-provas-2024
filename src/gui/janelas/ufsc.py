from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PyQt5 import QtGui
from .utiils import configurar_label_com_imagem, botaoGerarResultadosStyle, tituloTopoStyle, SelecionarDadosBrutosUfscStyle, SelecionarCaminhoUfscStyle, SelecionarCaminhoUfscStyle, SelecionarValeUfscGabaritoStyle, SelecionarInformaçõesUfscStyle, conversor_link, SelecionarCaminhoUfscRelatórioAlunosStyle, SelecionarValeUfscGabaritoConvertidoStyle
from src.alternatives.alternatives import gerar_grafico_distruibuicao
from src.invokers.ufsc_invokers import main

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
            "salvar_arquivos":"",
            "salvar_arquivos_alunos":"",
            "gabarito_vale_convertido":"",
            "gabarito_vale_csv":""

        }

        botaoGerarResultados = QPushButton("GerarResultados", self)
        botaoGerarResultados.move(290,525)
        botaoGerarResultados.resize(200,65)
        botaoGerarResultados.setStyleSheet(botaoGerarResultadosStyle)
        botaoGerarResultados.clicked.connect(
            lambda:main(self.CaminhosDeArquivos["dados_brutos"],
                        self.CaminhosDeArquivos["salvar_arquivos"],
                        self.CaminhosDeArquivos["gabarito_vale_csv"], 
                        self.CaminhosDeArquivos["salvar_arquivos_alunos"],
                        self.CaminhosDeArquivos["gabarito_vale_convertido"]))

        tituloTopo = QLabel(self)
        tituloTopo.setText("UFSC")
        tituloTopo.setGeometry(350, 20, 450, 100)  # x,y,width, height
        tituloTopo.setStyleSheet(tituloTopoStyle)

        # conversorLink = QLabel(self)
        # conversor_texto = f'''
        #     <a href="{conversor_link}" style="color: #ee7867; font-family: 'Cyrillic'; font-size: 20px;">
        #         {"Conversor"}
        #     </a>
        # '''
        # conversorLink.setText(conversor_texto)
        # conversorLink.setGeometry(530, 205, 100, 100)  # x,y,width, height
        # conversorLink.setStyleSheet(tituloTopoStyle)
        # conversorLink.setOpenExternalLinks(True)

        self.icon = QLabel(self)
        configurar_label_com_imagem(self.icon, "./assets/icons/einsteinlogo.png", 100, 100, 30, 470)
    

        # Criação do QPushButton
        self.SelecionarDadosBrutos = QPushButton("Selecionar dados brutos", self)
        self.SelecionarDadosBrutos.setObjectName("dados_brutos")
        self.SelecionarDadosBrutos.move(180,200)
        self.SelecionarDadosBrutos.resize(200,65)
        self.SelecionarDadosBrutos.setStyleSheet(SelecionarDadosBrutosUfscStyle)
        self.SelecionarDadosBrutos.clicked.connect(self.open_file_dialog)

        self.SelecionarGabaritoValeConvertido = QPushButton("Selecionar gabarito vale convertido", self)
        self.SelecionarGabaritoValeConvertido.setObjectName("gabarito_vale_convertido")
        self.SelecionarGabaritoValeConvertido.move(400,200)
        self.SelecionarGabaritoValeConvertido.resize(200,65)
        self.SelecionarGabaritoValeConvertido.setStyleSheet(SelecionarValeUfscGabaritoConvertidoStyle)
        self.SelecionarGabaritoValeConvertido.clicked.connect(self.open_file_dialog)

        self.SelecionarInformações = QPushButton("Selecionar infos alunos", self)
        self.SelecionarInformações.setObjectName("infos_alunos")
        self.SelecionarInformações.move(400,280)
        self.SelecionarInformações.resize(200,65)
        self.SelecionarInformações.setStyleSheet(SelecionarInformaçõesUfscStyle)
        self.SelecionarInformações.clicked.connect(self.open_file_dialog)

        self.SelecionarGabaritoValeCSV = QPushButton("Selecionar gabarito vale CSV", self)
        self.SelecionarGabaritoValeCSV.setObjectName("gabarito_vale_csv")
        self.SelecionarGabaritoValeCSV.move(180,280)
        self.SelecionarGabaritoValeCSV.resize(200,65)
        self.SelecionarGabaritoValeCSV.setStyleSheet(SelecionarValeUfscGabaritoStyle)
        self.SelecionarGabaritoValeCSV.clicked.connect(self.open_file_dialog)

        self.SelecionarCaminho = QPushButton("Caminho dos arquivos", self)
        self.SelecionarCaminho.setObjectName("salvar_arquivos")
        self.SelecionarCaminho.move(180,420)
        self.SelecionarCaminho.resize(200,65)
        self.SelecionarCaminho.setStyleSheet(SelecionarCaminhoUfscStyle)
        self.SelecionarCaminho.clicked.connect(self.openDirectory)

        self.SelecionarCaminhoRelatórioAlunos = QPushButton("Caminho dos relatorios individuais", self)
        self.SelecionarCaminhoRelatórioAlunos.setObjectName("salvar_arquivos_alunos")
        self.SelecionarCaminhoRelatórioAlunos.move(400,420)
        self.SelecionarCaminhoRelatórioAlunos.resize(200,65)
        self.SelecionarCaminhoRelatórioAlunos.setStyleSheet(SelecionarCaminhoUfscRelatórioAlunosStyle)
        self.SelecionarCaminhoRelatórioAlunos.clicked.connect(self.openDirectory)

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

    
    def openDirectory(self):
        options = QFileDialog.Options()
        folder = QFileDialog.getExistingDirectory(self, "Selecione o Diretório", "", options=options)
        button = self.sender()
        if folder:
            self.CaminhosDeArquivos[button.objectName()] = folder
            button_name = button.objectName()
            print(button_name)
            button.setText(f"Arquivo selecionado: {folder}")
            print(f"Diretório selecionado: {folder}")
            # Aqui você pode adicionar lógica para salvar o caminho selecionado para uso futuro

    
    def textoDeStatus(self):
        textoDeStatus = QLabel(self)
        textoDeStatus.setText("Variaveis Criadas!")
        textoDeStatus.setGeometry(220, 450, 450, 100)  # x,y,width, height
        textoDeStatus.setStyleSheet(tituloTopoStyle)


