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
         


import os,re
from PyQt5.QtWidgets import  QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QRadioButton, QHBoxLayout, QFileDialog #,QApplication


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                
#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3


class FileProcessor:
    def remove_regex(self, folder, regex_list, include_subfolders):
        # Compiling all the chosen regular expression patterns
        regex_patterns = [re.compile(regex) for regex in regex_list]

        # Searching all the files in all the folders of the selected directory
        for subdir, _, files in os.walk(folder):
            if not include_subfolders and subdir != folder:
                continue

            for filename in files:
                new_filename = filename

                # Applying all the regular expressions to our new file name
                for regex in regex_patterns:
                    new_filename = regex.sub('', new_filename)

                if new_filename != filename:
                    old_path = os.path.join(subdir, filename)
                    new_path = os.path.join(subdir, new_filename)

                    if os.path.exists(new_path):
                        new_name = self.get_unique_filename(subdir, new_filename)
                        new_path = os.path.join(subdir, new_name)

                    os.rename(old_path, new_path)



    def get_unique_filename(self, folder, filename):
        base, ext = os.path.splitext(filename)
        num = 1
        new_name = filename

        # Adding "duplicate name + number" before the extension if file name is duplicate
        while os.path.exists(os.path.join(folder, new_name)):
            new_name = f"{base}__DUPLICATE NAME{num}__{ext}"
            num += 1

        return new_name





class killerName(QDialog):
    def __init__(self):
        super().__init__()

        self.folder = None

        self.GUI()


    def launch(self):
        # Selecting the source folder
        self.folder = QFileDialog.getExistingDirectory(self, "Select a folder:")
        if not self.folder:
            return

        # Getting regular expressions from the input line
        regex_list = [self.regex_input.text().strip()]

        include_subfolders = self.radio_subfolder.isChecked()

        # Creating an instance of FileProcessor and calling remove_regex method
        processor = FileProcessor()
        processor.remove_regex(self.folder, regex_list, include_subfolders)

        # Displaying a message box that the process was successful
        QMessageBox.information(self, "Information", "I am in the process of correctly sorting and removing all of this.")



#____ ____ ____ ___  _  _ _ ____ ____ _       _  _ ____ ____ ____    _ _  _ ___ ____ ____ ____ ____ ____ ____ 
#| __ |__/ |__| |__] |__| | |    |__| |       |  | [__  |___ |__/    | |\ |  |  |___ |__/ |___ |__| |    |___ 
#|__] |  \ |  | |    |  | | |___ |  | |___    |__| ___] |___ |  \    | | \|  |  |___ |  \ |    |  | |___ |___ 


    def GUI(self):

        # Widget 
        self.radio_folder = QRadioButton('Folder')
        self.radio_subfolder = QRadioButton('With Subfolder')
        self.radio_subfolder.setToolTip("Take files from folder and subfolders")

        self.radio_folder.setChecked(True)

        self.regex_input = QLineEdit()
        self.regex_input.setPlaceholderText("Write the word to delete")


        launch_button = QPushButton('Launch')
        launch_button.clicked.connect(self.launch)


        # Layout 
        vLayRegexDel = QVBoxLayout()
        vLayRegexDel.addWidget(self.regex_input)

        hLayFolderOptions = QHBoxLayout()
        hLayFolderOptions.addWidget(self.radio_folder)
        hLayFolderOptions.addWidget(self.radio_subfolder)

        vLayRegexDel.addLayout(hLayFolderOptions)
        vLayRegexDel.addWidget(launch_button)

        self.setLayout(vLayRegexDel)


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                
#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3

#if __name__ == "__main__":
#    app = QApplication([])
#    window = killerName()
#    window.show()
#    app.exec_()
