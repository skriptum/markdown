from PySide6.QtGui import *
from PySide6.QtWidgets import *


class ServiceButton(QPushButton):
    def __init__(self, title, *args, **kwargs):
        super(ServiceButton, self).__init__(*args, **kwargs)
        
        self.setAutoFillBackground(True)

        self.setStyleSheet("style.qss")

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("RichMarkdown")
        self.bar = self.menuBar()

        layout = QGridLayout()
        layout.addWidget(ServiceButton("Youtube"))
        layout.addWidget(ServiceButton("Vimeo"))

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)