# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(428, 479)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"\n"
"background: qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.0791577, y2:0.125, stop:1 rgb(240,240,240), stop:0 rgb(210, 210, 210));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo_widget = QWidget(self.centralwidget)
        self.logo_widget.setObjectName(u"logo_widget")
        self.logo_widget.setEnabled(True)
        self.logo_widget.setStyleSheet(u"background:none;")
        self.horizontalLayout = QHBoxLayout(self.logo_widget)
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.text_label = QLabel(self.logo_widget)
        self.text_label.setObjectName(u"text_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_label.sizePolicy().hasHeightForWidth())
        self.text_label.setSizePolicy(sizePolicy)
        self.text_label.setMaximumSize(QSize(280, 100))
        font = QFont()
        font.setFamily(u"Avenir")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        self.text_label.setFont(font)
        self.text_label.setStyleSheet(u"border: none;\n"
"text-transform: uppercase;\n"
"font-size: 30pt;\n"
"background: none;")
        self.text_label.setFrameShape(QFrame.NoFrame)
        self.text_label.setTextFormat(Qt.AutoText)
        self.text_label.setPixmap(QPixmap(u":/icon/img/font_transp.png"))
        self.text_label.setScaledContents(True)
        self.text_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.text_label)


        self.verticalLayout.addWidget(self.logo_widget)

        self.service_widget = QWidget(self.centralwidget)
        self.service_widget.setObjectName(u"service_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.service_widget.sizePolicy().hasHeightForWidth())
        self.service_widget.setSizePolicy(sizePolicy1)
        self.service_widget.setStyleSheet(u"background-color:  white;\n"
"color: black;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.service_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.youtube_button = QPushButton(self.service_widget)
        self.youtube_button.setObjectName(u"youtube_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.youtube_button.sizePolicy().hasHeightForWidth())
        self.youtube_button.setSizePolicy(sizePolicy2)
        self.youtube_button.setMinimumSize(QSize(120, 80))
        self.youtube_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(222, 122, 63, 255), stop:0.980296 rgba(168, 0, 0, 255));\n"
"qproperty-icon: url(:/logos/youtube);\n"
"\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 3px solid black; \n"
"border-bottom: 3px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(222, 122, 63, 255), stop:0 rgba(168, 0, 0, 255));\n"
"}")
        self.youtube_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.youtube_button, 1, 2, 1, 1)

        self.drive_button = QPushButton(self.service_widget)
        self.drive_button.setObjectName(u"drive_button")
        sizePolicy2.setHeightForWidth(self.drive_button.sizePolicy().hasHeightForWidth())
        self.drive_button.setSizePolicy(sizePolicy2)
        self.drive_button.setMinimumSize(QSize(120, 80))
        self.drive_button.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:\n"
"    qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.157975, y2:0.170455, stop:0 rgba(120, 190, 0, 255), stop:1 rgba(17, 107, 118, 255));\n"
"qproperty-icon: url(:/logos/drive);\n"
"\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 3px solid black; \n"
"border-bottom: 3px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.157975, y2:0.170455, stop:1 rgba(120, 190, 0, 255), stop:0 rgba(17, 107, 118, 255));\n"
"}")
        self.drive_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.drive_button, 3, 1, 1, 1)

        self.vimeo_button = QPushButton(self.service_widget)
        self.vimeo_button.setObjectName(u"vimeo_button")
        sizePolicy2.setHeightForWidth(self.vimeo_button.sizePolicy().hasHeightForWidth())
        self.vimeo_button.setSizePolicy(sizePolicy2)
        self.vimeo_button.setMinimumSize(QSize(120, 80))
        self.vimeo_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(116, 171, 241, 255), stop:1 rgba(39, 44, 172, 255));\n"
"qproperty-icon: url(:/logos/vimeo);\n"
"\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 3px solid black; \n"
"border-bottom: 3px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(116, 171, 241, 255), stop:0 rgba(39, 44, 172, 255));\n"
"}")
        self.vimeo_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.vimeo_button, 1, 1, 1, 1)

        self.twitter_button = QPushButton(self.service_widget)
        self.twitter_button.setObjectName(u"twitter_button")
        sizePolicy2.setHeightForWidth(self.twitter_button.sizePolicy().hasHeightForWidth())
        self.twitter_button.setSizePolicy(sizePolicy2)
        self.twitter_button.setMinimumSize(QSize(120, 80))
        self.twitter_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(76, 181, 173, 255), stop:1 rgba(145, 188, 222, 255));\n"
"qproperty-icon: url(:/logos/twitter);\n"
"\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 3px solid black; \n"
"border-bottom: 3px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(76, 181, 173, 255), stop:0 rgba(145, 188, 222, 255));\n"
"}")
        self.twitter_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.twitter_button, 1, 3, 1, 1)

        self.pdf_button = QPushButton(self.service_widget)
        self.pdf_button.setObjectName(u"pdf_button")
        self.pdf_button.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pdf_button.sizePolicy().hasHeightForWidth())
        self.pdf_button.setSizePolicy(sizePolicy2)
        self.pdf_button.setMinimumSize(QSize(120, 80))
        self.pdf_button.setAutoFillBackground(False)
        self.pdf_button.setStyleSheet(u"\n"
"QPushButton  {\n"
"background:\n"
"    qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(80, 96, 190, 255), stop:1 rgba(216, 50, 222, 255));\n"
"qproperty-icon: url(:/logos/pdf);\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 3px solid black; \n"
"border-bottom: 3px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
" qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(80, 96, 190, 255), stop:0 rgba(216, 50, 222, 255))\n"
"\n"
"}")
        self.pdf_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.pdf_button, 3, 2, 1, 1)

        self.codepen_button = QPushButton(self.service_widget)
        self.codepen_button.setObjectName(u"codepen_button")
        sizePolicy2.setHeightForWidth(self.codepen_button.sizePolicy().hasHeightForWidth())
        self.codepen_button.setSizePolicy(sizePolicy2)
        self.codepen_button.setMinimumSize(QSize(120, 80))
        self.codepen_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(121, 190, 80, 255), stop:1 rgba(216, 222, 50, 255));\n"
"qproperty-icon: url(:/logos/codepen);\n"
"\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 3px solid black; \n"
"border-bottom: 3px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(121, 190, 80, 255), stop:0 rgba(216, 222, 50, 255));\n"
"}")
        self.codepen_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.codepen_button, 4, 1, 1, 1)

        self.website_button = QPushButton(self.service_widget)
        self.website_button.setObjectName(u"website_button")
        self.website_button.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.website_button.sizePolicy().hasHeightForWidth())
        self.website_button.setSizePolicy(sizePolicy2)
        self.website_button.setMinimumSize(QSize(120, 80))
        self.website_button.setAutoFillBackground(False)
        self.website_button.setStyleSheet(u"\n"
"QPushButton  {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(190, 170, 80, 255), stop:1 rgba(222, 115, 0, 255));\n"
"qproperty-icon: url(:/logos/website);\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 3px solid black; \n"
"border-bottom: 3px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(190, 170, 80, 255), stop:0 rgba(222, 115, 0, 255));\n"
"}")
        self.website_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.website_button, 3, 3, 1, 1)

        self.jsfiddle_button = QPushButton(self.service_widget)
        self.jsfiddle_button.setObjectName(u"jsfiddle_button")
        sizePolicy2.setHeightForWidth(self.jsfiddle_button.sizePolicy().hasHeightForWidth())
        self.jsfiddle_button.setSizePolicy(sizePolicy2)
        self.jsfiddle_button.setMinimumSize(QSize(120, 80))
        self.jsfiddle_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(168, 137, 255, 255), stop:1 rgba(38, 28, 123, 255));\n"
"qproperty-icon: url(:/logos/jsfiddle);\n"
"\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 3px solid black; \n"
"border-bottom: 3px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(168, 137, 255, 255), stop:0 rgba(38, 28, 123, 255));\n"
"}")
        self.jsfiddle_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.jsfiddle_button, 4, 2, 1, 1)

        self.github_button = QPushButton(self.service_widget)
        self.github_button.setObjectName(u"github_button")
        sizePolicy2.setHeightForWidth(self.github_button.sizePolicy().hasHeightForWidth())
        self.github_button.setSizePolicy(sizePolicy2)
        self.github_button.setMinimumSize(QSize(120, 80))
        self.github_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.881892, y1:0.869318, x2:0.281128, y2:0.398, stop:0 rgba(105, 105, 105, 255), stop:1 rgba(235, 235, 235, 255));\n"
"qproperty-icon: url(:/logos/github);\n"
"\n"
"border-radius:\n"
"    10px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 3px solid black; \n"
"border-bottom: 3px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.881892, y1:0.869318, x2:0.281128, y2:0.398, stop:1 rgba(105, 105, 105, 255), stop:0 rgba(235, 235, 235, 255));\n"
"}")
        self.github_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.github_button.setText(u"")
        self.github_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.github_button, 4, 3, 1, 1)

        self.label_2 = QLabel(self.service_widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamily(u"Avenir")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border: none;\n"
"text-transform: uppercase;\n"
"font-size: 20pt;\n"
"background: none;")
        self.label_2.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.service_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pdf_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_label.setText("")
#if QT_CONFIG(tooltip)
        self.youtube_button.setToolTip(QCoreApplication.translate("MainWindow", u"Embed a Youtube Video", None))
#endif // QT_CONFIG(tooltip)
        self.youtube_button.setText("")
#if QT_CONFIG(tooltip)
        self.drive_button.setToolTip(QCoreApplication.translate("MainWindow", u"Embed a Document from Google Drive or Docs", None))
#endif // QT_CONFIG(tooltip)
        self.drive_button.setText("")
#if QT_CONFIG(tooltip)
        self.vimeo_button.setToolTip(QCoreApplication.translate("MainWindow", u"Embed a Vimeo Video", None))
#endif // QT_CONFIG(tooltip)
        self.vimeo_button.setText("")
#if QT_CONFIG(tooltip)
        self.twitter_button.setToolTip(QCoreApplication.translate("MainWindow", u"Embed a Tweet", None))
#endif // QT_CONFIG(tooltip)
        self.twitter_button.setText("")
#if QT_CONFIG(tooltip)
        self.pdf_button.setToolTip(QCoreApplication.translate("MainWindow", u"Embed an online PDF", None))
#endif // QT_CONFIG(tooltip)
        self.pdf_button.setText("")
#if QT_CONFIG(tooltip)
        self.codepen_button.setToolTip(QCoreApplication.translate("MainWindow", u"Embed a Pen from CodePen", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.codepen_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.codepen_button.setText("")
#if QT_CONFIG(tooltip)
        self.website_button.setToolTip(QCoreApplication.translate("MainWindow", u"Embed a Website", None))
#endif // QT_CONFIG(tooltip)
        self.website_button.setText("")
#if QT_CONFIG(tooltip)
        self.jsfiddle_button.setToolTip(QCoreApplication.translate("MainWindow", u"Embed a Fiddle from JSFiddle", None))
#endif // QT_CONFIG(tooltip)
        self.jsfiddle_button.setText("")
#if QT_CONFIG(tooltip)
        self.github_button.setToolTip(QCoreApplication.translate("MainWindow", u"Embed a Gist or Github File with syntax highlighting", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.github_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Services", None))
    # retranslateUi

