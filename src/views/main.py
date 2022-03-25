#pyside6
from PySide6.QtWidgets import QMainWindow
#gui
from src.controllers.main_gui import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi(self)

        ####################################
        ##### SHOW MAIN WINDOW
        ###################################
        self.show()

        self.__signals_inputs()
        self.__signals_buttons()

    def __signals_inputs(self):
        self.input_url_download.returnPressed.connect(self.__enter_key_action)
    
    def __signals_buttons(self):
        self.button_download.clicked.connect(self.__enter_key_action)
    
    def __enter_key_action(self):
        self.__validate_url_youtube()

    def __validate_url_youtube(self):
        if(len(self.input_url_download.text()) != 0):
            print("url valida")
        else:
            print("ingrese una url valida")
            