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

dadosBrutosArquivoStyle = '''
        QLabel {
                text-align:center;
                font-family:"Cyrillic";   
                font-size:15px;
                color:black;  
                background-color:#239B56 ;
                border-radius:6px;
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

SelecionarDadosBrutosStyle= '''
            QPushButton {
                background-color: #00422b;
                border-radius: 6px;
                color: #e7e6e3;
                font-size:15px;
            }
            QPushButton:hover {
                background-color: #00734a;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        '''

SelecionarInformaçõesStyle = '''
        QPushButton {
                background-color: #00422b;
                border-radius: 6px;
                color: #e7e6e3;
                font-size:15px;
            }
            QPushButton:hover {
                background-color: #00734a;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        '''


SelecionarCaminhoStyle ='''
            QPushButton {
                background-color: #00422b;
                border-radius: 6px;
                color: #e7e6e3;
                font-size:15px;
            }
            QPushButton:hover {
                background-color: #117A65;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        '''


SelecionarDadosBrutosUfscStyle= '''
            QPushButton {
                background-color: #ee7867;
                border-radius: 6px;
                color: #e7e6e3;
                font-size:15px;
            }
            QPushButton:hover {
                background-color: #00734a;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        '''

SelecionarCaminhoUfscStyle= '''
            QPushButton {
                background-color: #ee7867;
                border-radius: 6px;
                color: #e7e6e3;
                font-size:15px;
            }
            QPushButton:hover {
                background-color: #00734a;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        '''

SelecionarValeUfscGabaritoStyle= '''
            QPushButton {
                background-color: #ee7867;
                border-radius: 6px;
                color: #e7e6e3;
                font-size:15px;
            }
            QPushButton:hover {
                background-color: #00734a;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        '''

SelecionarCaminhoUfscStyle= '''
            QPushButton {
                background-color: #ee7867;
                border-radius: 6px;
                color: #e7e6e3;
                font-size:15px;
            }
            QPushButton:hover {
                background-color: #00734a;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        '''

SelecionarInformaçõesUfscStyle = '''
            QPushButton {
                background-color: #ee7867;
                border-radius: 6px;
                color: #e7e6e3;
                font-size:15px;
            }
            QPushButton:hover {
                background-color: #00734a;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        '''

SelecionarCaminhoUfscRelatórioAlunosStyle = '''
            QPushButton {
                background-color: #ee7867;
                border-radius: 6px;
                color: #e7e6e3;
                font-size:15px;
            }
            QPushButton:hover {
                background-color: #00734a;
            }
            QPushButton:pressed {
                background-color: #f6f7fa;
            }
        '''

como_usar_link = "https://docs.google.com/document/d/14yY2QmvND_kaA3LWouWetNRXmbLeKBW7rhUjmy-KXFo/edit?usp=sharing"

como_usar_link_style = "color: #e5e5e5; font-family: 'Cyrillic'; font-size: 16px;"
conversor_link = "https://www.convertcsv.com/csv-to-json.htm"


versão_style = '''
            QLabel {
                font-family: "Cyrillic";   
                font-size: 13px;      
                background-color: transparent;
            }
        '''
        