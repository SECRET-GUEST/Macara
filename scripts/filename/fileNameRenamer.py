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
                
#       |                           This program converts copy then rename                  |                                           |               |                                           |               |                                           |                    |                                           |
                
#                          /                      |    v    |                    \
                
#                   all images from a chosen folder or folder & subfolders by 1, 2 ,3 ...        |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |  
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
         

import os
import shutil
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QComboBox #,QApplication


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                
#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3


# Processing Class
class ImageRenamer:
    def __init__(self, source_folder, target_folder, option):
        self.source_folder = source_folder
        self.target_folder = target_folder
        self.option = option

    def copy_and_rename(self):
        # Create a new folder in the target directory with the same name as the source folder
        target_path = os.path.join(self.target_folder, os.path.basename(self.source_folder))
        os.makedirs(target_path, exist_ok=True)

        # Iterate through the source folder
        for item in os.listdir(self.source_folder):
            src_path = os.path.join(self.source_folder, item)

            # Copy files or subfolders based on the option selected
            if os.path.isfile(src_path):
                shutil.copy(src_path, target_path)

            elif os.path.isdir(src_path) and self.option == "Folder and Subfolders":
                shutil.copytree(src_path, os.path.join(target_path, item))

        # Rename images in the target folder
        for subdir, _, files in os.walk(target_path):
            counter = 1

            for filename in files:
                extension = os.path.splitext(filename)[1].lower()

                # Check for valid image extensions
                if extension in ['.bmp', '.dib', '.dcx', '.gif', '.im', '.jpg', '.jpe', '.jpeg', '.pcd', '.pcx', '.png', '.pbm', '.pgm', '.ppm', '.psd', '.tif', '.tiff', '.xbm', '.xpm', '.pdf']:
                    new_name = str(counter) + extension
                    counter += 1

                    old = os.path.join(subdir, filename)
                    new = os.path.join(subdir, new_name)

                    os.rename(old, new)

# Fashion class
class oneToThree(QWidget):
    def __init__(self):
        super().__init__()
        self.source_folder = None
        self.target_folder = None
        self.GUI()

    def select_source_folder(self):
        # Select the source folder
        self.source_folder = QFileDialog.getExistingDirectory(self, "Select Source Folder")

    def initiate_renaming(self):
        self.rename_button.setEnabled(False)  # Disable the rename button during processing

        try:
            # Select the target folder
            self.target_folder = QFileDialog.getExistingDirectory(self, "Select Target Folder")

            # Initialize the ImageRenamer class and perform the copy and renaming process
            renamer = ImageRenamer(self.source_folder, self.target_folder, self.selection_combo.currentText())
            renamer.copy_and_rename()

            QMessageBox.information(self, "Information", "All images have been renamed.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            self.rename_button.setEnabled(True)  # Re-enable the rename button



#____ ____ ____ ___  _  _ _ ____ ____ _       _  _ ____ ____ ____    _ _  _ ___ ____ ____ ____ ____ ____ ____ 
#| __ |__/ |__| |__] |__| | |    |__| |       |  | [__  |___ |__/    | |\ |  |  |___ |__/ |___ |__| |    |___ 
#|__] |  \ |  | |    |  | | |___ |  | |___    |__| ___] |___ |  \    | | \|  |  |___ |  \ |    |  | |___ |___ 
   

    def GUI(self):
        # Widgets
        self.select_folder_button = QPushButton("Select Source Folder")
        self.select_folder_button.clicked.connect(self.select_source_folder)

        self.selection_combo = QComboBox()
        self.selection_combo.addItems(["Folder", "with Subfolders"])
        self.selection_combo.setToolTip("Take files from folder and subfolders")

        self.rename_button = QPushButton("Rename Images")
        self.rename_button.clicked.connect(self.initiate_renaming)

        # Layout
        self.VLayRenameSuit = QVBoxLayout()
        self.VLayRenameSuit.addWidget(self.select_folder_button)
        self.VLayRenameSuit.addWidget(self.selection_combo)
        self.VLayRenameSuit.addWidget(self.rename_button)
        self.setLayout(self.VLayRenameSuit)




#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3


#if __name__ == "__main__":
#    app = QApplication([])
#    rename_images_app = oneToThree()
#    rename_images_app.show()
#    app.exec_()


