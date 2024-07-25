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


