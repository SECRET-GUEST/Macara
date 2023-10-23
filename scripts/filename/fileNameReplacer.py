#      |               |                                 |
                
#                  |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#           |                                  |                                     |
                
#                  |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#   |                          |                       |                    |
#           |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#      |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                      |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#           |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                  |                     |
#   |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#           |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#   |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                               |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#                |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#        |                              Ce petit outils est a destination 
                
#                               d'un plus grand. Il permet de remplacer du texte                    |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
                
#                       des noms d'images, mais s'incorpore également facilement dans une         |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
#                                                                                                    |                                                                 |                      |                     |                       |                      |                     |                       |                      |                     |                            |
#                   fenetre externe. Cet outil a été construit pour Nathacha , artiste peintre 

#             de l'abstraction, vous pouvez retrouver son travail ici : https://www.artnathacha.com/
#      |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                                |                                   |     |                  
#                   |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#              |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                 |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                         =)
                
#
#                                |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#              |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#      |                        |                                         |                                |
                
#
#                                                     !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#      |               |                                 !
                
#                  |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#           |                                  !                                     |
                
#                  |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#   |                          |                       |                    !
#           |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
#      |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
                
#                      |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#           |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                                                |
                
#                  |                     |
#   |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |                                    |                       |                              |                                                                        |
#           |                               |                                         !                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
                

import os,re #,sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel, QLineEdit, QVBoxLayout,QHBoxLayout, QPushButton, QMessageBox, QRadioButton, QButtonGroup #,QApplication

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3




# Processing thread
class RenameThread(QThread):
    finished_signal = pyqtSignal(str)

    def __init__(self, folder, regex, replacement, process_subfolders):
        super().__init__()
        self.folder = folder
        self.regex = regex
        self.replacement = replacement
        self.process_subfolders = process_subfolders

    def run(self):
        for root, _, files in os.walk(self.folder):
            # If user chose not to process sub-folders, break after processing root folder
            if not self.process_subfolders and root != self.folder:
                break
            for file in files:
                if any(file.lower().endswith(ext) for ext in ['.bmp', '.dib', '.dcx', '.gif', '.im', '.jpg', '.jpe', '.jpeg', '.pcd', '.pcx', '.png', '.pbm', '.pgm', '.ppm', '.psd', '.tif', '.tiff', '.xbm', '.xpm', '.pdf']):
                    file_path = os.path.join(root, file)
                    new_file_name = re.sub(self.regex, self.replacement, file)
                    new_file_path = os.path.join(root, new_file_name)
                    os.rename(file_path, new_file_path)

        self.finished_signal.emit("Processing is complete!")




# Main window
class nameReplacer(QWidget):
    def __init__(self):
        super().__init__()
        self.GUI()

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select a folder")
        return folder

    def launch_rename(self):
        folder = self.select_folder()
        if not folder:
            return

        regex = self.txt_replace.text()
        replacement = self.txt_add.text()

        self.thread = RenameThread(folder, regex, replacement, self.radio_subfolder.isChecked())
        self.thread.finished_signal.connect(self.on_rename_completed)
        self.thread.start()

    def on_rename_completed(self, message):
        QMessageBox.information(self, "Finished", message)


#____ ____ ____ ___  _  _ _ ____ ____ _       _  _ ____ ____ ____    _ _  _ ___ ____ ____ ____ ____ ____ ____ 
#| __ |__/ |__| |__] |__| | |    |__| |       |  | [__  |___ |__/    | |\ |  |  |___ |__/ |___ |__| |    |___ 
#|__] |  \ |  | |    |  | | |___ |  | |___    |__| ___] |___ |  \    | | \|  |  |___ |  \ |    |  | |___ |___ 
   

    def GUI(self):
        self.setWindowTitle("Image Renamer")

        # Widgets
        self.lab_info = QLabel("Change words in image names:")

        self.lab_replace = QLabel("Replace:")
        self.txt_replace = QLineEdit()
        self.txt_replace.setPlaceholderText("Write the word to replace")

        self.lab_add = QLabel("by:")
        self.txt_add = QLineEdit()
        self.txt_add.setPlaceholderText("Write a word to add")

        self.radio_folder = QRadioButton("Folder")
        self.radio_subfolder = QRadioButton("With sub-folders")
        self.radio_subfolder.setToolTip("Take files from folder and subfolders")

        self.radio_folder.setChecked(True)

        self.radio_group = QButtonGroup(self)
        self.radio_group.addButton(self.radio_folder)
        self.radio_group.addButton(self.radio_subfolder)

        self.go_replacer = QPushButton("Replace words")
        self.go_replacer.clicked.connect(self.launch_rename)

        # Layout
        vlay_replace = QVBoxLayout()
        hlay_replace = QHBoxLayout()
        hlay_replace.addWidget(self.lab_replace)
        hlay_replace.addWidget(self.txt_replace)

        hlay_replace2 = QHBoxLayout()
        hlay_replace2.addWidget(self.lab_add)
        hlay_replace2.addWidget(self.txt_add)

        vlay_replace.addWidget(self.lab_info)
        vlay_replace.addLayout(hlay_replace)
        vlay_replace.addLayout(hlay_replace2)

        hLayRadio = QHBoxLayout()
        hLayRadio.addWidget(self.radio_folder)
        hLayRadio.addWidget(self.radio_subfolder)

        vlay_replace.addLayout(hLayRadio)
        vlay_replace.addWidget(self.go_replacer)

        self.setLayout(vlay_replace)




#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3


#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    renamer = nameReplacer()
#    renamer.show()
#    sys.exit(app.exec_())


