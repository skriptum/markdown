from PySide6.QtGui import *
from PySide6.QtWidgets import *

from dialog import Ui_Dialog
from functions import *

class DialogClass(QDialog, Ui_Dialog):
    def __init__(self, clipboard, *args, obj=None, **kwargs):
        """ set up a dialog , needs a clipboard"""
        super(DialogClass, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # define the clipboard
        self.clipboard = clipboard

        self.buttonBox.rejected.connect(self.cancel)
        self.buttonBox.accepted.connect(self.save_to_clipboard)

        self.create_button.clicked.connect(self.io_url)

    def io_url(self):
        url = self.text_input.text()

        txt = self.iframer(url)

        self.text_ouput.setPlainText(txt)
        self.create_button.setDefault(False)
        self.text_input.clear()

    def save_to_clipboard(self):
        txt = self.text_ouput.toPlainText()
        if len(txt) == 0:
            txt = self.io_url()
        self.clipboard.setText(txt)

        self.text_ouput.clear()
        self.reject()

    def cancel(self):
        self.text_ouput.setPlainText("")
        self.reject()

    def exec(self, service):
        self.service = service
        self.setWindowTitle(f"{service} to Markdown")
        self.exec_()

    def iframer(self, url):
        try:
            if self.service == "Youtube":
                return youtube_(url)
            if self.service == "Twitter":
                return twitter_(url)
            if self.service == "Vimeo":
                return vimeo_(url)
            if self.service == "GIPHY":
                return giphy_(url)
            if self.service == "Website":
                return website_(url)
            if self.service == "CodePen":
                return codepen_(url)
            if self.service == "JSFiddle":
                return jsfiddle_(url)
            if self.service == "GitHub":
                return github_(url)
            if self.service == "Gist":
                return gist_(url)
        except Exception as error:
            return str(error)