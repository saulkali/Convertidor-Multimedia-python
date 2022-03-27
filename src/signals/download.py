#pyside6
from PySide6.QtCore import QObject,Signal

class DownloadSignals(QObject):
    finish_download = Signal(list)
    status_download = Signal(str)