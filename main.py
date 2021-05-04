from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

# circular importing !
from dialogclass import DialogClass
from mainwindowclass import MainWindow

#set up the app
app = QApplication(sys.argv)
app.setApplicationName("Markdown")

app.setQuitOnLastWindowClosed(False)
app.setWindowIcon(QIcon(u":/icon/markdown.png"))

clipboard = app.clipboard() #needed in the dialog window class !

#set up the windows
app.dialog_window = DialogClass(clipboard)

main_window = MainWindow(app.dialog_window)


#all actions stuff
#-------------------------------------------------------------------------------

# Create the icon
icon = QIcon(u":/icon/icon.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)


# Create the menus
shortcut_menu = QMenu("Embeds")
#create custom menu for the main window
general_menu = QMenu("General")
media_menu = QMenu("Media")
code_menu = QMenu("Code")
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

window_action = QAction("Open Help")
window_action.triggered.connect(main_window.show)
window_action.setShortcut(QKeySequence("Ctrl+Shift+H"))
#-------------------------------------------------------------------------------

#add actions to the shortcut menu
shortcut_menu.addAction(website_action)
shortcut_menu.addSeparator()

shortcut_menu.addAction(youtube_action)
shortcut_menu.addAction(twitter_action)
shortcut_menu.addAction(vimeo_action)
#menu.addAction(giphy_action)
shortcut_menu.addSeparator()

shortcut_menu.addAction(codepen_action)
shortcut_menu.addAction(jsfiddle_action)
shortcut_menu.addAction(github_action)
shortcut_menu.addSeparator()

shortcut_menu.addAction(drive_action)
shortcut_menu.addSeparator()

shortcut_menu.addAction(quit_action)
shortcut_menu.addAction(window_action)


media_menu.addAction(youtube_action)
media_menu.addAction(twitter_action)
media_menu.addAction(vimeo_action)

general_menu.addAction(website_action)
general_menu.addAction(drive_action)

code_menu.addAction(codepen_action)
code_menu.addAction(jsfiddle_action)
code_menu.addAction(github_action)


#----------------------------
#add the menus to the window and tray
tray.setContextMenu(shortcut_menu)
main_window.bar.addMenu(general_menu)
main_window.bar.addMenu(media_menu)
main_window.bar.addMenu(code_menu)

#-------------------------------------------------------------------------------
# execute 
sys.exit(app.exec_())

