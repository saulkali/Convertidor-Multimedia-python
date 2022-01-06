from PySide6 import QtWidgets
from PySide6.QtWidgets import (QVBoxLayout, QLineEdit, QPushButton,QWidget, QHBoxLayout)

class Main_GUI(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)

        ##################################
        ##### GLOBAL VARS
        ##################################
        self.boxlayout = QVBoxLayout()

        #################################
        #### METHOD INIT
        #################################
        self.set_central_widget()
        self.set_style_sheet()
        self.set_widgets()

    def set_central_widget(self):
        widget = QWidget()
        widget.setLayout(self.boxlayout)
        self.setCentralWidget(widget)
    
    def set_style_sheet(self):
        pass

    def set_widgets(self): 
        ##################################
        ####### CREATE LAYOUTS
        #################################
        boxlayout_header = QHBoxLayout()
        self.boxlayout.addLayout(boxlayout_header)

        boxlayout_body = QHBoxLayout()
        self.boxlayout.addLayout(boxlayout_body)

        ##################################
        #####   CREATE BUTTONS
        #################################
        btn_add = QPushButton("Añadir Archivo")
        btn_add.setObjectName("buttonAdd")
        boxlayout_header.addWidget(btn_add)

        btn_delete = QPushButton("Eliminar")
        btn_delete.setObjectName("buttonDelete")
        boxlayout_header.addWidget(btn_delete)

        ###################################
        #### SIGNALS BUTTONS
        ###################################

