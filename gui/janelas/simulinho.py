from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel

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
        botaoGerarVariaveis.move(70,450)
        botaoGerarVariaveis.resize(300,100)
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
        botaoGerarResultados.move(400,450)
        botaoGerarResultados.resize(300,100)
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
        tituloTopo.setGeometry(300, 20, 450, 100)  # Ajusta o tamanho e a posição do QLabel
        tituloTopo.setStyleSheet(
            '''
            QLabel {font:bold;font-size:40px}
            
            ''')

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
