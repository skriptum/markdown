from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

# circular importing !
from dialogclass import DialogClass
from mainwindow import MainWindow

#set up the app
app = QApplication(sys.argv)
app.setApplicationName("Markdown")

app.setQuitOnLastWindowClosed(False)
app.setWindowIcon(QIcon(u":/icon/markdown.png"))

clipboard = app.clipboard() #needed in the dialog window class !

#set up the windows
app.dialog_window = DialogClass(clipboard)
app.main_window = MainWindow()

# Create the icon
icon = QIcon(u":/icon/icon.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()


#-----
# services = ["Website","Youtube", "Twitter", "Vimeo", "GIPHY", "CodePen"]

# action_list = []

# for s in services:
#     action = QAction(s)
#     action.triggered.connect(lambda s=s:app.dialog_window.exec(s)) #named vairiable fixes !
#       #not working, just last one

#     action_list.append(action)

# for i, ac in enumerate(action_list):
#     menu.addAction(ac)
#     if i in (0,4):
#         menu.addSeparator()
#-----

#-------------------------------------------------------------------------------
#create all actions
youtube_action = QAction("Youtube")
youtube_action.triggered.connect(lambda x:app.dialog_window.exec("Youtube"))
youtube_action.setIcon(QIcon(u":/logos/youtube"))

twitter_action = QAction("Twitter")
twitter_action.triggered.connect(lambda x:app.dialog_window.exec("Twitter"))
twitter_action.setIcon(QIcon(u":/logos/twitter"))

vimeo_action = QAction("Vimeo")
vimeo_action.triggered.connect(lambda x:app.dialog_window.exec("Vimeo"))
vimeo_action.setIcon(QIcon(u":/logos/vimeo"))

giphy_action = QAction("GIPHY")
giphy_action.triggered.connect(lambda x:app.dialog_window.exec("Giphy"))

website_action = QAction("Website")
website_action.triggered.connect(lambda x:app.dialog_window.exec("Website"))
website_action.setIcon(QIcon(u":/logos/website"))

codepen_action = QAction("CodePen")
codepen_action.triggered.connect(lambda x:app.dialog_window.exec("CodePen"))
codepen_action.setIcon(QIcon(u":/logos/codepen"))

jsfiddle_action = QAction("JSFiddle")
jsfiddle_action.triggered.connect(lambda x:app.dialog_window.exec("JSFiddle"))
jsfiddle_action.setIcon(QIcon(u":/logos/jsfiddle"))

github_action = QAction("GitHub")
github_action.triggered.connect(lambda x:app.dialog_window.exec("GitHub"))
github_action.setIcon(QIcon(u":/logos/github"))


drive_action = QAction("Google Drive")
drive_action.triggered.connect(lambda x:app.dialog_window.exec("Drive"))
drive_action.setIcon(QIcon(u":/logos/drive"))


# Add a Quit option to the menu.
quit_action = QAction("Quit")
quit_action.triggered.connect(app.quit)
quit_action.setShortcut(QKeySequence("Ctrl+Q"))

window_action = QAction("Open Window")
window_action.triggered.connect(app.main_window.exec_)
#-------------------------------------------------------------------------------

#add actions to the menu
menu.addAction(website_action)
menu.addSeparator()

menu.addAction(youtube_action)
menu.addAction(twitter_action)
menu.addAction(vimeo_action)
#menu.addAction(giphy_action)
menu.addSeparator()

menu.addAction(codepen_action)
menu.addAction(jsfiddle_action)
menu.addAction(github_action)
menu.addSeparator()

menu.addAction(drive_action)
menu.addSeparator()

menu.addAction(quit_action)
menu.addAction(window_action)

# Add the menu to the tray
tray.setContextMenu(menu)

#-------------------------------------------------------------------------------
# execute 
sys.exit(app.exec_())

