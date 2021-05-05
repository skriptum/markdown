# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(478, 364)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setAutoFillBackground(False)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 100))
        self.label_2.setPixmap(QPixmap(u":/logos/website"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 100))
        self.label_3.setPixmap(QPixmap(u":/icon/img/arrow.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.icon = QLabel(self.widget_2)
        self.icon.setObjectName(u"icon")
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMaximumSize(QSize(100, 100))
        self.icon.setPixmap(QPixmap(u":/icon/markdown.png"))
        self.icon.setScaledContents(True)
        self.icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.icon)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.text_input = QLineEdit(self.widget)
        self.text_input.setObjectName(u"text_input")

        self.horizontalLayout.addWidget(self.text_input)

        self.create_button = QPushButton(self.widget)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setEnabled(True)
        self.create_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.create_button)


        self.verticalLayout.addWidget(self.widget)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.error_label = QLabel(self.frame)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setEnabled(True)
        self.error_label.setStyleSheet(u"border: 2px solid rgba(200,0,0,1);\n"
"border-radius: 5px;\n"
"background: rgba(255, 38, 36, 162);\n"
"color: white;")

        self.verticalLayout.addWidget(self.error_label)

        self.text_ouput = QTextBrowser(self.frame)
        self.text_ouput.setObjectName(u"text_ouput")

        self.verticalLayout.addWidget(self.text_ouput)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Markdown", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.icon.setText("")
        self.text_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"paste url", None))
        self.create_button.setText(QCoreApplication.translate("Dialog", u"create", None))
        self.error_label.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Save stores the Output in your Clipboard", None))
    # retranslateUi

