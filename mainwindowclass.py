from PySide6.QtGui import *
from PySide6.QtWidgets import *

from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, dialog, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.dialog = dialog

        self.resize(400,400)
        self.bar = self.menuBar()
        self.setWindowTitle("RichMark")
        

        self.github_button.clicked.connect(lambda x: self.dialog.exec("GitHub"))