from PySide6.QtGui import *
from PySide6.QtWidgets import *

# circular importing !
from dialogclass import DialogClass

#set up the app
app = QApplication([])
app.setQuitOnLastWindowClosed(False)
app.setWindowIcon(QIcon(u":/icon/markdown.png"))
clipboard = app.clipboard()

#set up the window
app.dialog_window = DialogClass(clipboard)

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
#     action.triggered.connect(lambda x:app.dialog_window.exec(s)) 
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
youtube_action.setShortcut(QKeySequence("Ctrl+Y"))

twitter_action = QAction("Twitter")
twitter_action.triggered.connect(lambda x:app.dialog_window.exec("Twitter"))

vimeo_action = QAction("Vimeo")
vimeo_action.triggered.connect(lambda x:app.dialog_window.exec("Vimeo"))

giphy_action = QAction("GIPHY")
giphy_action.triggered.connect(lambda x:app.dialog_window.exec("Giphy"))

website_action = QAction("Website")
website_action.triggered.connect(lambda x:app.dialog_window.exec("Website"))
website_action.setShortcut(QKeySequence("Ctrl+W"))

codepen_action = QAction("CodePen")
codepen_action.triggered.connect(lambda x:app.dialog_window.exec("CodePen"))

jsfiddle_action = QAction("JSFiddle")
jsfiddle_action.triggered.connect(lambda x:app.dialog_window.exec("JSFiddle"))

github_action = QAction("GitHub")
github_action.triggered.connect(lambda x:app.dialog_window.exec("GitHub"))

gist_action = QAction("Gist")
gist_action.triggered.connect(lambda x:app.dialog_window.exec("Gist"))

# Add a Quit option to the menu.
quit_action = QAction("Quit")
quit_action.triggered.connect(app.quit)
quit_action.setShortcut(QKeySequence("Ctrl+Q"))
#-------------------------------------------------------------------------------

#add actions to the menu
menu.addAction(website_action)
menu.addSeparator()

menu.addAction(youtube_action)
menu.addAction(twitter_action)
menu.addAction(vimeo_action)
menu.addAction(giphy_action)
menu.addSeparator()

menu.addAction(codepen_action)
menu.addAction(jsfiddle_action)
menu.addAction(github_action)
menu.addAction(gist_action)
menu.addSeparator()

menu.addAction(quit_action)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec_()

