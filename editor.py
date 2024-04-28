import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction)
from PyQt5.QtGui import QKeySequence
from PIL import Image, ImageFilter

app = QApplication([])
win = QWidget()
win.resize(600,400)
win.setWindowTitle("Easy Editor")

lb_image= QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files =QListWidget()

btn_left = QPushButton("Вліво")
btn_left.setStyleSheet('''
    QPushButton {
        background-color: orange;
    }
    QPushButton:hover {
        background-color: red;
    }
''')

btn_right = QPushButton("Вправо")
btn_right.setStyleSheet('''
    QPushButton {
        background-color: black;
    }
    QPushButton {
        color: red;
    }
    QPushButton:hover {
        background-color: pink;
    }
''')

btn_flip = QPushButton('Відзеркалити')
btn_sharp = QPushButton('Різкість')
#ЛІНІЯ ДЛЯ КНОПОК
row = QHBoxLayout()
row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_flip)
row.addWidget(btn_sharp)
#ГОЛОВНА ЛІНІЯ 
col1= QVBoxLayout()
col2= QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)
col2.addLayout(row)
main_layout = QHBoxLayout()
main_layout.addLayout(col1)
main_layout.addLayout(col2)
win.setLayout(main_layout)
class Image():
    def __init__(self):
        self.filename = None
        self.original = None
        self.new_photo = None
        self.dir = "MainPhoto/"
        
    def do_bw(self):
        self.new_photo = self.new_photo.convert("L")
        
    
win.show()
app.exec_()