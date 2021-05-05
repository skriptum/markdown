from PySide6.QtGui import *
from PySide6.QtWidgets import *
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, dialog, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.dialog = dialog

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.resize(400,400)
        self.bar = self.menuBar()
        self.setWindowTitle("RichMark")

        #connect all the buttons
        self.github_button.clicked.connect(lambda x: self.dialog.exec("GitHub"))
        self.youtube_button.clicked.connect(lambda x: self.dialog.exec("Youtube"))
        self.vimeo_button.clicked.connect(lambda x: self.dialog.exec("Vimeo"))
        self.twitter_button.clicked.connect(lambda x: self.dialog.exec("Twitter"))
        self.drive_button.clicked.connect(lambda x: self.dialog.exec("Drive"))
        self.website_button.clicked.connect(lambda x: self.dialog.exec("Website"))
        self.codepen_button.clicked.connect(lambda x: self.dialog.exec("CodePen"))
        self.jsfiddle_button.clicked.connect(lambda x: self.dialog.exec("JSFiddle"))
        self.pdf_button.clicked.connect(lambda x: self.dialog.exec("PDF"))