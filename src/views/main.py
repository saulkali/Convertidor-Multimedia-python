from src.GUI.mainGUI import Main_GUI


class MainWindow(Main_GUI):
    def __init__(self, parent = None):
        super().__init__(parent = parent)


        ####################################
        ##### SHOW MAIN WINDOW
        self.show()