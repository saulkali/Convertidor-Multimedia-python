#pyside6
from PySide6.QtWidgets import QMainWindow,QHeaderView,QTableWidgetItem,QFileDialog
from PySide6.QtCore import QThreadPool

#thread
from src.threads.download_youtube import DownloadYoutubeThread

#gui
from src.controllers.main_gui import Ui_MainWindow

#pytube
import pytube

#settings
from src.lib.settings.settings_manager import SettingsManager

#entity
from src.entitys import Video

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi(self)

        ####################################
        ##### SHOW MAIN WINDOW
        ###################################
        self.show()

        self.__setup_table_widget_downloads()
        self.__setup_path_save_video()
        self.__signals_inputs()
        self.__signals_buttons()
    
    def __setup_path_save_video(self):
        str_path = SettingsManager().downloader.path_save
        self.input_path_save.setText(str_path.__str__())

    def __setup_table_widget_downloads(self):
        table = self.tableWidget.horizontalHeader()
        table.setSectionResizeMode(0,QHeaderView.Stretch)
        table.setSectionResizeMode(1,QHeaderView.Stretch)
        table.setSectionResizeMode(2,QHeaderView.Stretch)
        table.setSectionResizeMode(3,QHeaderView.Stretch)
        table.setSectionResizeMode(4,QHeaderView.Stretch)
        table.setSectionResizeMode(5,QHeaderView.Stretch)


    def __signals_inputs(self):
        self.input_url_download.returnPressed.connect(self.__enter_key_action)
    
    def __open_file_dialog(self):
        file_dialog = QFileDialog(self).show()

    def __signals_buttons(self):
        self.button_download.clicked.connect(self.__enter_key_action)
        self.button_open_path.clicked.connect(self.__open_file_dialog)

    def __enter_key_action(self):
        self.__validate_url_youtube()
    
    def __finish_download(self,msj:str):
        print(msj)
    
    def __add_download_in_table_widget(self,video_details:Video):
        n = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(n + 1)
        self.tableWidget.setItem(n,0,QTableWidgetItem(video_details.title))
    
    def __create_thread_pool_download(self,file_download):
        self.__thread_pool_download = QThreadPool()
        self.__thread_download = DownloadYoutubeThread(file_download = file_download)
        self.__thread_download.signals.finish_download.connect(self.__finish_download)
        self.__thread_pool_download.start(self.__thread_download)
    
    def __validate_url_youtube(self):
        if(len(self.input_url_download.text()) != 0):
            try:
                video_url = self.input_url_download.text()
                yt = pytube.YouTube(video_url)
                
                video_details = Video()
                video_details.title = yt.title
                self.__add_download_in_table_widget(video_details)

                video = yt.streams.get_highest_resolution()
                self.__create_thread_pool_download(file_download = video)
            
            except Exception as e:
                print(f"Error: {e}")
            
            print("url valida")
        else:
            print("ingrese una url valida")
            


#################
# referencias
#################
# https://stackoverflow.com/questions/49185538/how-to-add-progress-bar
#
#