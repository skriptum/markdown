# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(604, 510)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vimeo_button = QPushButton(self.widget)
        self.vimeo_button.setObjectName(u"vimeo_button")
        self.vimeo_button.setMinimumSize(QSize(100, 100))
        self.vimeo_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(116, 171, 241, 255), stop:1 rgba(39, 44, 172, 255));\n"
"qproperty-icon: url(:/logos/vimeo);\n"
"\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(116, 171, 241, 255), stop:0 rgba(39, 44, 172, 255));\n"
"}")
        self.vimeo_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.vimeo_button, 0, 1, 1, 1)

        self.youtube_button = QPushButton(self.widget)
        self.youtube_button.setObjectName(u"youtube_button")
        self.youtube_button.setMinimumSize(QSize(100, 100))
        self.youtube_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(222, 122, 63, 255), stop:0.980296 rgba(168, 0, 0, 255));\n"
"qproperty-icon: url(:/logos/youtube);\n"
"\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(222, 122, 63, 255), stop:0 rgba(168, 0, 0, 255));\n"
"}")
        self.youtube_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.youtube_button, 0, 2, 1, 1)

        self.map_button = QPushButton(self.widget)
        self.map_button.setObjectName(u"map_button")
        self.map_button.setMinimumSize(QSize(100, 100))
        self.map_button.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(190, 170, 80, 255), stop:1 rgba(222, 115, 0, 255));\n"
"qproperty-icon: url(:/logos/map);\n"
"\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(190, 170, 80, 255), stop:0 rgba(222, 115, 0, 255));\n"
"}")
        self.map_button.setIconSize(QSize(50, 50))
        self.map_button.setCheckable(False)

        self.gridLayout.addWidget(self.map_button, 2, 2, 1, 1)

        self.website_button = QPushButton(self.widget)
        self.website_button.setObjectName(u"website_button")
        self.website_button.setEnabled(True)
        self.website_button.setMinimumSize(QSize(100, 100))
        self.website_button.setAutoFillBackground(False)
        self.website_button.setStyleSheet(u"\n"
"QPushButton  {\n"
"background:\n"
"qlineargradient(spread:pad, x1:1, y1:0.511364, x2:0, y2:0.52841, stop:0 rgba(167, 99, 99, 255), stop:0.995074 rgba(45, 60, 98, 255));\n"
"qproperty-icon: url(:/logos/website);\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:1, y1:0.511364, x2:0, y2:0.52841, stop:1 rgba(167, 99, 99, 255), stop:0 rgba(45, 60, 98, 255));\n"
"}")
        self.website_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.website_button, 1, 1, 1, 1)

        self.twitter_button = QPushButton(self.widget)
        self.twitter_button.setObjectName(u"twitter_button")
        self.twitter_button.setMinimumSize(QSize(100, 100))
        self.twitter_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(76, 181, 173, 255), stop:1 rgba(145, 188, 222, 255));\n"
"qproperty-icon: url(:/logos/twitter);\n"
"\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(76, 181, 173, 255), stop:0 rgba(145, 188, 222, 255));\n"
"}")
        self.twitter_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.twitter_button, 0, 3, 1, 1)

        self.pdf_button = QPushButton(self.widget)
        self.pdf_button.setObjectName(u"pdf_button")
        self.pdf_button.setEnabled(True)
        self.pdf_button.setMinimumSize(QSize(100, 100))
        self.pdf_button.setAutoFillBackground(False)
        self.pdf_button.setStyleSheet(u"\n"
"QPushButton  {\n"
"background:\n"
"    qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(80, 96, 190, 255), stop:1 rgba(216, 50, 222, 255));\n"
"qproperty-icon: url(:/logos/pdf);\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
" qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(80, 96, 190, 255), stop:0 rgba(216, 50, 222, 255))\n"
"\n"
"}")
        self.pdf_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.pdf_button, 2, 3, 1, 1)

        self.drive_button = QPushButton(self.widget)
        self.drive_button.setObjectName(u"drive_button")
        self.drive_button.setMinimumSize(QSize(100, 100))
        self.drive_button.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:\n"
"    qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.157975, y2:0.170455, stop:0 rgba(120, 190, 0, 255), stop:1 rgba(17, 107, 118, 255));\n"
"qproperty-icon: url(:/logos/drive);\n"
"\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.157975, y2:0.170455, stop:1 rgba(120, 190, 0, 255), stop:0 rgba(17, 107, 118, 255));\n"
"}")
        self.drive_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.drive_button, 2, 1, 1, 1)

        self.codepen_button = QPushButton(self.widget)
        self.codepen_button.setObjectName(u"codepen_button")
        self.codepen_button.setMinimumSize(QSize(100, 100))
        self.codepen_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(121, 190, 80, 255), stop:1 rgba(216, 222, 50, 255));\n"
"qproperty-icon: url(:/logos/codepen);\n"
"\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(121, 190, 80, 255), stop:0 rgba(216, 222, 50, 255));\n"
"}")
        self.codepen_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.codepen_button, 1, 3, 1, 1)

        self.jsfiddle_button = QPushButton(self.widget)
        self.jsfiddle_button.setObjectName(u"jsfiddle_button")
        self.jsfiddle_button.setMinimumSize(QSize(100, 100))
        self.jsfiddle_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:0 rgba(168, 137, 255, 255), stop:1 rgba(38, 28, 123, 255));\n"
"qproperty-icon: url(:/logos/jsfiddle);\n"
"\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.896552, y1:0.903409, x2:0.138271, y2:0.170455, stop:1 rgba(168, 137, 255, 255), stop:0 rgba(38, 28, 123, 255));\n"
"}")
        self.jsfiddle_button.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.jsfiddle_button, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.github_button = QPushButton(self.widget_2)
        self.github_button.setObjectName(u"github_button")
        self.github_button.setMinimumSize(QSize(100, 100))
        self.github_button.setStyleSheet(u"\n"
"QPushButton {\n"
"background:\n"
"qlineargradient(spread:pad, x1:0.812808, y1:0.835, x2:0, y2:0.0227277, stop:0 rgba(173, 173, 173, 255), stop:1 rgba(0, 0, 0, 255));\n"
"qproperty-icon: url(:/logos/github);\n"
"\n"
"border-radius:\n"
"    15px;\n"
"border-style:\n"
"    solid;\n"
"border-width:\n"
"    0px;\n"
"border-color: \n"
"    black}\n"
"\n"
"QPushButton:hover {\n"
"border-right: 5px solid black; \n"
"border-bottom: 5px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: \n"
"qlineargradient(spread:pad, x1:0.812808, y1:0.835, x2:0, y2:0.0227277, stop:1 rgba(173, 173, 173, 255), stop:0 rgba(0, 0, 0, 255));\n"
"}")
        self.github_button.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.github_button)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pdf_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.vimeo_button.setText("")
        self.youtube_button.setText("")
        self.map_button.setText("")
        self.website_button.setText("")
        self.twitter_button.setText("")
        self.pdf_button.setText("")
        self.drive_button.setText("")
#if QT_CONFIG(tooltip)
        self.codepen_button.setToolTip(QCoreApplication.translate("MainWindow", u"CodePen", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.codepen_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.codepen_button.setText("")
        self.jsfiddle_button.setText("")
#if QT_CONFIG(statustip)
        self.github_button.setStatusTip(QCoreApplication.translate("MainWindow", u"GitHub", None))
#endif // QT_CONFIG(statustip)
        self.github_button.setText("")
    # retranslateUi

