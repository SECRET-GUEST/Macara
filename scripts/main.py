#     |               |                                 |
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  |                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    |
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                 |                     |
#  |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#          |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#  |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#               |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#       |                              Main script to manage several things                    |                                           |               |                                           |               |                                           |                    |                                           |
                
#                          /                      |    v    |                    \
                
#                   like the graphical user interface, style, tabs, and also add some menus       |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |  
#     |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                               |                                   |     |                  
#                  |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#             |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                        =)
                
#
#                               |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#             |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#     |                        |                                         |                                |
                
#
#                                                    !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#     |               |                                 !
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  !                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    !
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                                                |
              
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|


from PyQt5.QtWidgets import QMainWindow,QMenu, QAction,QDialog,QPushButton,QLabel,QVBoxLayout,QTextEdit, QApplication, QTabWidget, QDockWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys


# Handlers
from handlers.zoom_handler import enable_zoom
from handlers.logInfo import logz
from handlers.cypunk1 import cypunk3MainWindow


# Images
from images.img2Gif import gifMaker
from images.imgConverter import imgConverter
from images.imgPixelizer import pixelize
from images.imgQrusher import Qrusher
from images.imgRembg import remBackBatch
from images.imgResizer import ImageResizer

# File names
from filename.fileNameRandonamer import Randonamers
from filename.fileNameRegexRemover import killerName
from filename.fileNameRenamer import oneToThree
from filename.fileNameReplacer import nameReplacer
from filename.fileNameWatermark import watermarker


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3



logger = None #To use Logger in all applications


# Faster to integrate with this window's inception method 
# TODO : rework.class windowCeption(cypunk1Window) to integrate the 2nd main window

class windowCeption(cypunk3MainWindow):
    def __init__(self):
        super().__init__(
            title="Oh hi Mark",
            window_size=("300x100"),
            btn_minimize="assets/ico/hide.png",
            btn_show="assets/ico/open.png",
            stylesheet_path= None
        )
        global logger
        # If logger is provided, use it, otherwise create a new logz object with the specified settings
        self.logger = logger or logz.configLogs("Macara", "ERRORS.log", use_qt_dialogs=True)

        # Create an instance of logz to access the ThemeChangedSignal class
        logz_instance = logz("")

        # Create an instance of ThemeChangedSignal to manage theme change events
        self.theme_changed_signal = logz_instance.ThemeChangedSignal()

        # Load the last used theme from the configuration file
        last_theme = self.logger.load_config()

        # Update the theme of the window based on the last used theme
        self.logger.update_theme(self, last_theme)

        # Connect the theme_changed signal to the update_theme_slot method to handle theme changes
        self.theme_changed_signal.theme_changed.connect(self.update_theme_slot)

        # Configure the error handler
        #self.tables = DarthBMO(self.logger)

        # Put the main app in the custom window represented by this class
        self.Vlay = QVBoxLayout()
        self.main_page = MainWindow(parent=self)
        #self.main_page.set_overlay(self.overlay)
        self.Vlay.addSpacing(28)
        self.Vlay.addWidget(self.main_page)

        self.central_widget.setLayout(self.Vlay)

    # Update themes
    def update_theme_slot(self, theme):
        self.logger.update_theme(self, theme)



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the logger, overlay, and tables attributes from the parent window
        self.logger = parent.logger
        #self.overlay = parent.overlay
        #self.tables = parent.tables
        #self.recorder = parent.recorder

        # Theme initialization
        self.theme_changed_signal = parent.theme_changed_signal

        # Create a dictionary to store widget instances
        self.widget_instances = {}

        # Enable zooming for this window
        enable_zoom(self)

        self.setWindowIcon(QIcon(self.logger.ressource_path("assets/ico/macara.png")))

        self.initUI()
        self.initMenu()



    # Connect the theme_changed signal to the update_theme_slot method of the Overlay instance
    def set_overlay(self, overlay_instance):
        self.overlay = overlay_instance
        self.theme_changed_signal.theme_changed.connect(self.overlay.update_theme_slot)

        # Add the Overlay instance to the widget_instances dictionary
        self.widget_instances["overlay"] = self.overlay

    def update_all_widgets_theme(self, theme):
        for widget_instance in self.widget_instances.values():
            self.logger.update_theme(widget_instance, theme)












#____ ___ _  _ ____ ____    ____ _  _ _  _ ____ ___ _ ____ _  _ ____ 
#|  |  |  |__| |___ |__/    |___ |  | |\ | |     |  | |  | |\ | [__  
#|__|  |  |  | |___ |  \    |    |__| | \| |___  |  | |__| | \| ___] 
                                                                    


    # Launches or closes the specified program tab within the tabWidget
    def launchProgram(self, programClass, tabWidget, checked, name):
        if checked:
            programApp = programClass()             # Create an instance of the specified program class
            tabWidget.addTab(programApp, name)      # Add the program as a new tab with the given name
        else:
            # Loop through the tabs and find the one corresponding to the program class
            for index in range(tabWidget.count()):
                if tabWidget.widget(index).__class__ == programClass:
                    tabWidget.removeTab(index)     # Remove the tab when found
                    break


    # Adds a program action to the specified menu
    def addProgram(self, menu, name, function):
        program_action = QAction(name, self, checkable=True) # Create an action with the given name and checkable option
        program_action.triggered.connect(function)           # Connect the action to the provided function
        menu.addAction(program_action)                        # Add the action to the menu


    # Toggles the visibility of the imagesDock
    def toggleImagesDock(self, checked):
        if checked:
            self.imagesDock.show()      
        else:
            self.imagesDock.hide()      


    # Toggles the visibility of the nameHandlersDock
    def toggleNameHandlersDock(self, checked):
        if checked:
            self.nameHandlersDock.show()    
        else:
            self.nameHandlersDock.hide() 



    def about_dialog(self):
        # Open a dialog box showing information about the program
        self.about_dial = QDialog(self)
        self.about_dial.setWindowTitle("About")
        self.about_dial.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        about_text = (
"Apologies for any false 'malware' alerts that may have been triggered. "
"The licensing cost for this software is $500 for 6 months, which is why it hasn't been acquired yet.<br><br>"
"Remember that software is free and was initially developed for personal use.<br>"
"I am now sharing it with others aims to help those in search of a good solution.<br>"
"Feel free to follow the project and contribute at: <br><br>"
"<a href='https://github.com/SECRET-GUEST/Macara'>SECRET-GUEST/Macara</a><br><br>"
"Please note that this version might not be completely stable and could occasionally crash. "
"Nevertheless, its features should work well for most users. Testing it on every machine isn't feasible, "
"so if an issue arises, kindly report it at: <br><br>"
"<a href='https://github.com/SECRET-GUEST/Macara/issues'>Report an issue on SECRET-GUEST/Macara</a><br><br>"
"Every effort will be made to address reported issues. Thank you."

        )

        self.about_dial_label = QLabel(about_text, self.about_dial)
        self.about_dial_label.setOpenExternalLinks(True)
        self.about_dial_label.setTextFormat(Qt.RichText)
        self.about_dial_label.setWordWrap(True)

        self.close_button = QPushButton("Close", self.about_dial)
        self.close_button.clicked.connect(self.about_dial.close)

        self.Vlay_about = QVBoxLayout(self.about_dial)
        self.Vlay_about.addWidget(self.about_dial_label)
        self.Vlay_about.addWidget(self.close_button)
        self.about_dial.exec_()




    def help_dialog(self):
        # Read the Markdown file
        with open(self.logger.ressource_path('handlers/README.md'), 'r', encoding='utf-8') as file:
            md_content = file.read()

        # Display the plain text content in a QDialog
        self.help_dial = QDialog(self)
        self.help_dial.setWindowTitle("Help")
        self.help_dial.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.text_view = QTextEdit(self.help_dial)
        self.text_view.setPlainText(md_content)
        self.text_view.setReadOnly(True)
        self.Vlay_help = QVBoxLayout(self.help_dial)
        self.Vlay_help.addWidget(self.text_view)
        self.help_dial.exec_()







#____ ____ ____ ___  _  _ _ ____ ____ _       _  _ ____ ____ ____    _ _  _ ___ ____ ____ ____ ____ ____ ____ 
#| __ |__/ |__| |__] |__| | |    |__| |       |  | [__  |___ |__/    | |\ |  |  |___ |__/ |___ |__| |    |___ 
#|__] |  \ |  | |    |  | | |___ |  | |___    |__| ___] |___ |  \    | | \|  |  |___ |  \ |    |  | |___ |___ 
   

    def initMenu(self):
        menu_bar = self.menuBar()

        # Menu "Settings"
        settings_menu = QMenu("Settings", self)
        menu_bar.addMenu(settings_menu)

        self.themes_action = QAction("Themes", self)
        self.themes_action.setShortcut("Ctrl+T")
        self.themes_action.triggered.connect(lambda: self.logger.change_theme(self, self.theme_changed_signal))

        settings_menu.addAction(self.themes_action)

        # Add all image programs on startup
        self.launchProgram(imgConverter, self.imagesTabWidget, True, "Converter")
        self.launchProgram(gifMaker, self.imagesTabWidget, True, "GIF Maker")
        self.launchProgram(pixelize, self.imagesTabWidget, True, "Pixelize")
        self.launchProgram(remBackBatch, self.imagesTabWidget, True, "Change Background")
        self.launchProgram(ImageResizer, self.imagesTabWidget, True, "Resizer")
        self.launchProgram(Qrusher, self.imagesTabWidget, True, "Weightless")
        
        # Add all name handlers programs on startup
        self.launchProgram(Randonamers, self.nameHandlersTabWidget, True, "Randomize")
        self.launchProgram(killerName, self.nameHandlersTabWidget, True, "Delete")
        self.launchProgram(oneToThree, self.nameHandlersTabWidget, True, "1,2,3...")
        self.launchProgram(nameReplacer, self.nameHandlersTabWidget, True, "Replace")
        self.launchProgram(watermarker, self.nameHandlersTabWidget, True, "Watermark")
        

        # Menu "Windows"
        windows_menu = menu_bar.addMenu("Windows")
        self.show_images_dock_action = QAction("Show Images", self, checkable=True)
        self.show_images_dock_action.triggered.connect(self.toggleImagesDock)
        windows_menu.addAction(self.show_images_dock_action)

        self.show_name_handlers_dock_action = QAction("Show Name Handlers", self, checkable=True)
        self.show_name_handlers_dock_action.triggered.connect(self.toggleNameHandlersDock)
        windows_menu.addAction(self.show_name_handlers_dock_action)

        #Menu Help
        help_menu = QMenu("Help", self)
        menu_bar.addMenu(help_menu)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.about_dialog)
        help_menu.addAction(about_action)

        help_action = QAction("?", self)
        help_action.triggered.connect(self.help_dialog)
        help_menu.addAction(help_action)





    def initUI(self):
        # Set dock tab positions to top
        self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)

        # Dock for Images
        self.imagesDock = QDockWidget("Images", self)
        self.imagesDock.visibilityChanged.connect(lambda visible: self.show_images_dock_action.setChecked(visible))
        self.imagesDock = QDockWidget("Images", self)
        self.imagesTabWidget = QTabWidget()
        self.imagesDock.setWidget(self.imagesTabWidget)
        self.imagesDock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.imagesDock)

        # Dock for Name Handlers
        self.nameHandlersDock = QDockWidget("Name handlers", self)
        self.nameHandlersDock.visibilityChanged.connect(lambda visible: self.show_name_handlers_dock_action.setChecked(visible))
        self.nameHandlersTabWidget = QTabWidget()
        self.nameHandlersDock.setWidget(self.nameHandlersTabWidget)
        self.nameHandlersDock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.addDockWidget(Qt.RightDockWidgetArea, self.nameHandlersDock)




#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = windowCeption()
    mainApp.show()
    sys.exit(app.exec_())
