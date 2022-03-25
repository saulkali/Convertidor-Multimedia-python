###########################################################################
#nombre: convertidor multimedia
#autor: saul burciaga hernandez
#correo: saulburciagahernandez@hotmail.com
#creado: 25 de marzo del 2022
#Copyright     (c) 2021 by saul burciaga hernandez, 2021 
#token access: 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
###########################################################################

__version__ = "1.0.0.0"

DEBUG = False

# pyside6
from PySide6 import QtWidgets

# views
from src.views import MainWindow

# utilies
import sys 

def production():
    app = QtWidgets.QApplication(sys.argv)
    window_main = MainWindow()
    sys.exit(app.exec())

def debug():
    print("debug enabled")

if __name__ == "__main__":
    if DEBUG:
        debug()
    else:
        production()