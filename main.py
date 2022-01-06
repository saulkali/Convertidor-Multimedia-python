# pyside6
from PySide6 import QtWidgets

# views
from src.views import MainWindow

# utilies
import sys 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_main = MainWindow()
    sys.exit(app.exec())