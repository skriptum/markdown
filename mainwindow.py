from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("RichMarkdown")