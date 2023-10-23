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
                
#                               d'un plus grand. Il permet d'ajouter du texte dans                    |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
                
#                       Le nom d'images, mais s'incorpore également facilement dans une         |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
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
from PyQt5.QtWidgets import  QFileDialog, QLabel, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QPushButton, QRadioButton, QHBoxLayout #,QApplication



#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3

class WatermarkProcessor:
    def process(self, folder, watermark_text, include_subfolders=False):
        # Traverse all the folders in the selected directory
        for subdir, _, files in os.walk(folder):
            for file in files:  # Check if there are images that PIL can read, regardless of capitalization
                if any(file.lower().endswith(ext) for ext in ['.bmp', '.dib', '.dcx', '.gif', '.im', '.jpg', '.jpe', '.jpeg', '.pcd', '.pcx', '.png', '.pbm', '.pgm', '.ppm', '.psd', '.tif', '.tiff', '.xbm', '.xpm', '.pdf']):

                    # If yes, import the file path
                    base, ext = os.path.splitext(file)
                    new_name = f"{base},{watermark_text}{ext}"

                    # To avoid errors, check if the file name already exists, otherwise rename
                    i = 1

                    while os.path.exists(os.path.join(subdir, new_name)):
                        new_name = f"{base}_DUPLICATE NAME{i}_{watermark_text}{ext}"
                        i += 1

                    # Finally, rename the image with the new name
                    try:
                        old_path = os.path.join(subdir, file)
                        new_path = os.path.join(subdir, new_name)
                        os.rename(old_path, new_path)

                    except Exception as e:
                        QMessageBox.critical(self, "ERROR", str(e))


            if not include_subfolders:
                break




class watermarker(QWidget):
    def __init__(self):
        super().__init__()

        self.GUI()



    # Function to select the folder
    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select folder")
        return folder



    # Function to add the chosen text
    def watermarking(self, watermark_text):

        # Accepts uppercase and lowercase letters but not symbols
        if not re.match("^[a-zA-Z ]*$", watermark_text):
            QMessageBox.information(self, "Information", "Alphabet only!")
            return

        # Call the folder
        folder = self.select_folder()
        if not folder:
            return

        include_subfolders = self.rad_subfolders.isChecked()

        self.watermark_button.setDisabled(True)

        processor = WatermarkProcessor()
        processor.process(folder, watermark_text, include_subfolders)

        QMessageBox.information(self, "Information", "I have renamed all the images in the selected folder.")
        self.watermark_button.setDisabled(False)




#____ ____ ____ ___  _  _ _ ____ ____ _       _  _ ____ ____ ____    _ _  _ ___ ____ ____ ____ ____ ____ ____ 
#| __ |__/ |__| |__] |__| | |    |__| |       |  | [__  |___ |__/    | |\ |  |  |___ |__/ |___ |__| |    |___ 
#|__] |  \ |  | |    |  | | |___ |  | |___    |__| ___] |___ |  \    | | \|  |  |___ |  \ |    |  | |___ |___ 
   


    def GUI(self):
        self.setWindowTitle("Add words to the end of the image name")

        # Widgets
        self.lab_watermark = QLabel()
        self.lab_watermark.setText("Add words to the end of the image names:")

        self.ent_watermark = QLineEdit()
        self.ent_watermark.setPlaceholderText("Write a watermark (no symbols)")

        self.radio_folder = QRadioButton("Folder Only")
        self.radio_subfolders = QRadioButton("With Subfolders")
        self.radio_subfolders.setToolTip("Take files from folder and subfolders")

        self.radio_folder.setChecked(True) 



        self.watermark_button = QPushButton()
        self.watermark_button.setText("Add words")

        # Connect the button to the function to keep the text
        self.watermark_button.clicked.connect(lambda: self.watermarking(self.ent_watermark.text()))

        # Layouts

        self.Vlay_fili = QVBoxLayout()
        self.Vlay_fili.addSpacing(10)
        self.Vlay_fili.addWidget(self.lab_watermark)
        self.Vlay_fili.addSpacing(2)
        self.Vlay_fili.addWidget(self.ent_watermark)

        self.HLayRadio = QHBoxLayout()
        self.HLayRadio.addWidget(self.radio_folder)
        self.HLayRadio.addWidget(self.radio_subfolders)

        self.Vlay_fili.addLayout(self.HLayRadio)
        self.Vlay_fili.addSpacing(10)
        self.Vlay_fili.addWidget(self.watermark_button)

        self.setLayout(self.Vlay_fili)


#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3

#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    fili_pop_up = watermarker()
#    fili_pop_up.show()
#    sys.exit(app.exec_())
