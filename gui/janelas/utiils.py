import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def configurar_label_com_imagem(label: QLabel, file_path: str, width: int, height: int, x: int, y: int):
    # Carrega e redimensiona o QPixmap
    pixmap = QPixmap(file_path)
    scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    
    # Configura o QPixmap no QLabel
    label.setPixmap(scaled_pixmap)
    
    # Configura o tamanho e a posição do QLabel
    label.setGeometry(x, y, width, height)

SimulinhoBotaoStyle = '''
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
        '''

EnemBotaoStyle = '''
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
        '''

UfscBotaoStyle = '''
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
        '''

UdescBotaoStyle = '''
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
        '''

PsBotaoStyle = '''
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
        '''

tituloTopoStyle = '''
            QLabel {
                font-family: "Cyrillic";   
                font-size: 32px;      
                background-color: transparent;
            }
        '''

botaoGerarVariaveisStyle = '''
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
        '''

botaoGerarResultadosStyle = '''
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
        ''' 
