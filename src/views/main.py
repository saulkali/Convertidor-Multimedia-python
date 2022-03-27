#pyside6
from PySide6.QtWidgets import (QMainWindow,QHeaderView,QTableWidgetItem,
                                QFileDialog,QAbstractItemView,QMessageBox,
                                QProgressBar)

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

        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def __signals_inputs(self):
        self.input_url_download.returnPressed.connect(self.__enter_key_action)
    
    def __open_file_dialog(self):
        path_dir = QFileDialog.getExistingDirectory(self,"Select Directory")
        if len(path_dir) != 0:
            self.__set_path_save_video(path_dir)
    
    def __set_path_save_video(self,path):
        self.input_path_save.setText(path)

    def __signals_buttons(self):
        self.button_download.clicked.connect(self.__enter_key_action)
        self.button_open_path.clicked.connect(self.__open_file_dialog)

    def __enter_key_action(self):
        self.__validate_url_youtube()
    
    def __finish_download(self,data:list):
        position = data[0]
        message = data[1]
        
        item = self.tableWidget.item(position,2)
        if item is not None:
            item.setText(message)

    
    def __add_download_in_table_widget(self,video_details:Video,file_download):
        position = self.tableWidget.rowCount()
        progressbar = QProgressBar(self)
        progressbar.setRange(0,int(video_details.file_size))
        progressbar.setValue(10000)
        
        self.tableWidget.setRowCount(position + 1)
        self.tableWidget.setItem(position,0,QTableWidgetItem(video_details.title))
        self.tableWidget.setCellWidget(position,1,progressbar)
        self.tableWidget.setItem(position,2,QTableWidgetItem("downloading..."))
        self.tableWidget.setItem(position,3,QTableWidgetItem(video_details.file_size))
        self.tableWidget.setItem(position,4,QTableWidgetItem("mp4"))
        self.tableWidget.setItem(position,5,QTableWidgetItem(video_details.url))


        self.__create_thread_pool_download(
            file_download = file_download,
            position = position
        )

    def __create_thread_pool_download(self,file_download,position):
        self.__thread_pool_download = QThreadPool()
        self.__thread_download = DownloadYoutubeThread(
            file_download = file_download,
            position = position)
        self.__thread_download.signals.finish_download.connect(self.__finish_download)
        self.__thread_pool_download.start(self.__thread_download)

    def __validate_url_youtube(self):
        if(len(self.input_url_download.text()) != 0):
            try:
                video_url = self.input_url_download.text()
                
                yt = pytube.YouTube(video_url)
                video = yt.streams.get_highest_resolution()
                
                video_details = Video()
                video_details.title = yt.title
                video_details.file_size = video.filesize.__str__()
                video_details.url = video_url

                self.__add_download_in_table_widget(
                    video_details = video_details,
                    file_download = video)

            except Exception as e:
                msj = QMessageBox()
                msj.setWindowTitle("Error:")
                msj.setText("url no valida.")
                msj.exec()

            self.input_url_download.setText("")
        else:
            msj = QMessageBox()
            msj.setWindowTitle("Error:")
            msj.setText("Ingrese una url.")
            msj.exec()
            


#################
# referencias
#################
# https://stackoverflow.com/questions/49185538/how-to-add-progress-bar
#
#