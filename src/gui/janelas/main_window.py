import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.topo = 200
        self.lado = 550
        self.largura = 800
        self.altura = 600
        self.titulo = "Corretor de Simulados"
        
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv)

j = Janela()
sys.exit(aplicacao.exec_())