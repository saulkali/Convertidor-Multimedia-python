#pyside6
from PySide6.QtCore import QRunnable,Slot

#signals
from src.signals.download import DownloadSignals

#helper
from helper import exists_dir,getFile,absPath

class DownloadYoutubeThread(QRunnable):
    def __init__(self,file_download) -> None:
        super().__init__()
        self.file_download = file_download       
        self.signals = DownloadSignals()
    
    @Slot()
    def run(self):
        print("download process")
        print(f"""
            title:{self.file_download.title}
        """)
        try:
            self.file_download.download(absPath("videos/"))
            self.signals.finish_download.emit("download success")
        except:
            print("error con la red...")