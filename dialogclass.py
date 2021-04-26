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

        #for the buttons and their interplay, disable the save button when initiated
        self.create_button.setDefault(True)
        self.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)

    def io_url(self):
        url = self.text_input.text()

        try:
            txt = self.iframer(url)

            #button operations, enable save button an set Default
            self.create_button.setDefault(False)
            bt = self.buttonBox.button(QDialogButtonBox.Save)
            bt.setEnabled(True)
            bt.setDefault(True)
        except Exception as Error:
            txt = str(Error)

        self.text_ouput.setPlainText(txt)
        self.text_input.clear()

    def save_to_clipboard(self):
        txt = self.text_ouput.toPlainText()
        if len(txt) == 0:
            txt = self.io_url()
        self.clipboard.setText(txt)

        self.text_ouput.clear()
        self.close()

    def cancel(self):
        self.text_ouput.setPlainText("")
        self.reject()

    def exec(self, service):
        self.service = service
        self.setWindowTitle(f"{service} to Markdown")
        self.label_2.setPixmap(QPixmap(f":/logos/{service.lower()}"))
        self.exec_()

    def iframer(self, url):
    
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
            return decider_(url)
        if self.service == "Drive":
            return google_drive_(url)
