#pyside6
from PySide6.QtCore import QRunnable,Slot

#signals
from src.signals.download import DownloadSignals

#helper
from src.lib.settings.settings_manager import SettingsManager

class DownloadYoutubeThread(QRunnable):
    def __init__(self,file_download,position:int) -> None:
        super().__init__()
        self.file_download = file_download       
        self.signals = DownloadSignals()
        self.path = SettingsManager().downloader.path_save
        self.position = position

    @Slot()
    def run(self):
        print("download process")
        print(f"""
            title:{self.file_download.title}
            file_size: {self.file_download.filesize}
        """)
        try:
            self.file_download.download(self.path)
            data = []
            data.append(self.position) 
            data.append("Success")
            self.signals.finish_download.emit(data)
        except Exception as e:
            data = []
            data.append(self.position) 
            data.append("Error de red")  
            self.signals.finish_download.emit(data)
            print(f"Error: {e}")