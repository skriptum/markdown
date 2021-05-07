from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property

from PySide2.QtWidgets import *
from PySide2.QtGui import *

import sys

#beware of circular importing !
from dialogclass import DialogClass
from mainwindowclass import MainWindow


class AppContext(ApplicationContext):

    def __init__(self, *args, **kwargs):
        super(AppContext, self).__init__(*args, **kwargs)

        self.app.setQuitOnLastWindowClosed(False)

    @cached_property
    def dialog_window(self):
        return DialogClass(self.app.clipboard(), self.tray)

    @cached_property
    def main_window(self):
        return MainWindow(self.dialog_window)
    
    @cached_property
    def tray(self):
        tray = QSystemTrayIcon()
        # Create the icon
        icon = QIcon(u":/icon/logo_white")

        #style the try
        tray.setIcon(icon)
        tray.setVisible(True)

        return tray

    def run(self):
        self.main_window.show()
        self.setup_actions()
        return self.app.exec_()

    def setup_actions(self):
        #all actions stuff
        #-------------------------------------------------------------------------------
        # Create the menus
        self.shortcut_menu = QMenu("Embeds")
        #create custom menu for the main window
        self.general_menu = QMenu("General")
        self.media_menu = QMenu("Media")
        self.code_menu = QMenu("Code")
        #-------------------------------------------------------------------------------
        #create all actions
        youtube_action = QAction("Youtube", self.app)
        youtube_action.triggered.connect(lambda x:self.dialog_window.exec("Youtube"))
        youtube_action.setIcon(QIcon(u":/logos/youtube"))

        twitter_action = QAction("Twitter", self.app)
        twitter_action.triggered.connect(lambda x:self.dialog_window.exec("Twitter"))
        twitter_action.setIcon(QIcon(u":/logos/twitter"))

        vimeo_action = QAction("Vimeo", self.app)
        vimeo_action.triggered.connect(lambda x:self.dialog_window.exec("Vimeo"))
        vimeo_action.setIcon(QIcon(u":/logos/vimeo"))

        giphy_action = QAction("GIPHY",self.app)
        giphy_action.triggered.connect(lambda x:self.dialog_window.exec("Giphy"))

        website_action = QAction("Website", self.app)
        website_action.triggered.connect(lambda x:self.dialog_window.exec("Website"))
        website_action.setIcon(QIcon(u":/logos/website"))

        codepen_action = QAction("CodePen", self.app)
        codepen_action.triggered.connect(lambda x:self.dialog_window.exec("CodePen"))
        codepen_action.setIcon(QIcon(u":/logos/codepen"))

        jsfiddle_action = QAction("JSFiddle", self.app)
        jsfiddle_action.triggered.connect(lambda x:self.dialog_window.exec("JSFiddle"))
        jsfiddle_action.setIcon(QIcon(u":/logos/jsfiddle"))

        github_action = QAction("GitHub", self.app)
        github_action.triggered.connect(lambda x:self.dialog_window.exec("GitHub"))
        github_action.setIcon(QIcon(u":/logos/github"))


        drive_action = QAction("Google Drive", self.app)
        drive_action.triggered.connect(lambda x:self.dialog_window.exec("Drive"))
        drive_action.setIcon(QIcon(u":/logos/drive"))

        pdf_action = QAction("PDF", self.app)
        pdf_action.triggered.connect(lambda x:self.dialog_window.exec("PDF"))
        pdf_action.setIcon(QIcon(u":/logos/pdf"))

        # Add a Quit option to the menu.
        quit_action = QAction("Quit", self.app)
        quit_action.triggered.connect(self.app.quit)
        quit_action.setShortcut(QKeySequence("Ctrl+Q"))

        window_action = QAction("Open Window", self.app)
        window_action.triggered.connect(self.main_window.show)
        window_action.setShortcut(QKeySequence("Ctrl+O"))
        #-------------------------------------------------------------------------------

        #add actions to the shortcut menu
        self.shortcut_menu.addAction(website_action)
        self.shortcut_menu.addSeparator()

        self.shortcut_menu.addAction(youtube_action)
        self.shortcut_menu.addAction(twitter_action)
        self.shortcut_menu.addAction(vimeo_action)
        #menu.addAction(giphy_action)
        self.shortcut_menu.addSeparator()

        self.shortcut_menu.addAction(codepen_action)
        self.shortcut_menu.addAction(jsfiddle_action)
        self.shortcut_menu.addAction(github_action)
        self.shortcut_menu.addSeparator()

        self.shortcut_menu.addAction(drive_action)
        self.shortcut_menu.addAction(pdf_action)
        self.shortcut_menu.addSeparator()

        self.shortcut_menu.addAction(window_action)
        self.shortcut_menu.addAction(quit_action)

        # add actions to the window menu
        self.media_menu.addAction(youtube_action)
        self.media_menu.addAction(twitter_action)
        self.media_menu.addAction(vimeo_action)

        self.general_menu.addAction(website_action)
        self.general_menu.addAction(drive_action)
        self.general_menu.addAction(pdf_action)

        self.code_menu.addAction(codepen_action)
        self.code_menu.addAction(jsfiddle_action)
        self.code_menu.addAction(github_action)


        #----------------------------
        #add the menus to the window and tray
        self.tray.setContextMenu(self.shortcut_menu)
        self.main_window.bar.addMenu(self.general_menu)
        self.main_window.bar.addMenu(self.media_menu)
        self.main_window.bar.addMenu(self.code_menu)




#-------------------------------------------------------------------------------
# execute 

if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)