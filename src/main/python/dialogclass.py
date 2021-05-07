from PySide2.QtGui import *
from PySide2.QtWidgets import *

from dialog import Ui_Dialog
from functions import *

class DialogClass(QDialog, Ui_Dialog):
    def __init__(self, clipboard, tray, *args, obj=None, **kwargs):
        """ set up a dialog , needs a clipboard"""
        super(DialogClass, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        #set the red error label to invisble
        self.error_label.setVisible(False)

        # define the clipboard
        self.clipboard = clipboard
        self.tray = tray

        #connect the buttons
        self.buttonBox.rejected.connect(self.cancel)
        self.buttonBox.accepted.connect(self.save_to_clipboard)

        self.create_button.clicked.connect(self.io_url)

        self.button_reset()

    #set buttons to start position
    def button_reset(self):
        #for the buttons and their interplay, disable the save button when initiated
        self.create_button.setDefault(True)
        self.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)

    #function for the working of the URLs
    def io_url(self):
        url = self.text_input.text()

        try:
            txt = self.iframer(url)

            #button operations, enable save button an set Default
            self.create_button.setDefault(False)
            bt = self.buttonBox.button(QDialogButtonBox.Save)
            bt.setEnabled(True)
            bt.setDefault(True)

            self.text_ouput.setPlainText(txt)
            self.error_label.setVisible(False)

        #show the error label
        except Exception as Error:
            txt = str(Error)
            self.error_label.setVisible(True)
            self.error_label.setText(txt)

        self.text_input.clear()

    #get the text, save it and clear everything and close
    def save_to_clipboard(self):
        txt = self.text_ouput.toPlainText()
        if len(txt) == 0:
            txt = self.io_url()
        self.clipboard.setText(txt)

        self.tray.showMessage("Markdown Embedder","copied embed code to clipboard",self.tray.NoIcon,  3000)

        self.text_ouput.clear()
        self.button_reset()
        self.close()

    #on cancel buttn press clear the output, hide the error label and close
    def cancel(self):
        self.text_ouput.setPlainText("")
        self.error_label.setVisible(False)
        self.reject()

    #execute the window and style it with title and icon according to Service
    def exec(self, service):
        self.service = service
        self.setWindowTitle(f"{service} to Markdown")
        self.label_2.setPixmap(QPixmap(f":/logos/{service.lower()}"))

        self.error_label.setVisible(False)
        
        self.exec_()

    #call the corresponding function to a Service
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
        if self.service == "PDF":
            return pdf_(url)
