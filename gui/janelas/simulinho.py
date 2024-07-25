from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
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
        # Conectar o botão ao método desejado
        # botaoGerarVariaveis.clicked.connect(self.Simulinho)

        botaoGerarResultados = QPushButton("GerarResultados", self)
        botaoGerarResultados.move(450,450)
        botaoGerarResultados.resize(200,60)
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

        tituloTopo = QLabel(self)
        tituloTopo.setText("Simulinho")
        tituloTopo.setGeometry(320, 20, 450, 100)  # Ajusta o tamanho e a posição do QLabel. Pode ser usado o resize tambem
        tituloTopo.setStyleSheet(
            '''
            QLabel {font-size:32px;font-family:Cyrillic}
            
            ''')


    def CarregarJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
