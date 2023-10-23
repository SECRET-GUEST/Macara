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
                
#       |                           This program converts a folder of images                  |                                           |               |                                           |               |                                           |                    |                                           |
                
#                          /                      |    v    |                    \
                
#                   into an animated GIF, with options for frame per seconds and resizing.        |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |  
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
         

import  os, imageio #,sys
from PIL import Image
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtWidgets import  QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QFileDialog, QWidget, QCheckBox, QComboBox, QMessageBox,QLabel #,QApplication


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                
#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3

class ConversionThread(QThread):
    # Signal to be emitted in case of error during conversion
    errorOccurred = pyqtSignal(str)

    def __init__(self, directory, fps, resize_images, scale_width, resize_mode, output_file_name, filenames):
        """
        Initialize the conversion thread.

        :param directory: Directory containing the images to be converted.
        :param fps: Frames per second for the GIF.
        :param resize_images: Whether to resize images or not.
        :param scale_width: Target width for resizing.
        :param resize_mode: Resizing algorithm to use (e.g., Nearest, Bilinear).
        :param output_file_name: Output file name for the GIF.
        :param filenames: List of filenames to be converted.
        """
        super().__init__()
        self.directory = directory
        self.fps = fps
        self.resize_images = resize_images
        self.scale_width = scale_width if resize_images else None
        self.resize_mode = resize_mode
        self.output_file_name = output_file_name
        self.filenames = filenames

    def run(self):
        """
        Convert images in the specified directory to a GIF.

        Images are resized based on the given width and resizing mode, maintaining the aspect ratio.
        Unsupported file types are skipped, and an error is emitted if the conversion fails.
        """
        images = []
        try:
            for filename in self.filenames:
                filepath = os.path.join(self.directory, filename)
                if not filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.jfif')):
                    continue
                img = Image.open(filepath)
                if self.resize_images and self.scale_width:
                    # Calculate the target aspect ratio
                    target_ratio = self.scale_width / (self.scale_width * img.size[1] / img.size[0])
                    original_ratio = img.size[0] / img.size[1]

                    # Crop the image to match the target aspect ratio
                    if original_ratio > target_ratio:
                        new_width = int(target_ratio * img.size[1])
                        offset = (img.size[0] - new_width) // 2
                        img = img.crop((offset, 0, img.size[0] - offset, img.size[1]))
                    else:
                        new_height = int(img.size[0] / target_ratio)
                        offset = (img.size[1] - new_height) // 2
                        img = img.crop((0, offset, img.size[0], img.size[1] - offset))

                    # Resize the image based on the given width and resizing mode
                    img = img.resize((self.scale_width, int(self.scale_width * img.size[1] / img.size[0])), getattr(Image, self.resize_mode.upper()))

                images.append(img)

            # Save the images as a GIF
            imageio.mimsave(self.output_file_name, images, fps=self.fps)
            self.finished.emit()
        except Exception as e:
            # Emit an error signal if the conversion fails
            self.errorOccurred.emit(str(e))





class gifMaker(QWidget):
    def __init__(self):
        """
        Initialize the gifMaker widget.
        This sets up the UI elements required for user interaction.
        """
        super().__init__()
        self.GUI()



    def browse_directory(self):
        """
        Open a dialog for the user to select a directory containing images.
        Sets the selected directory to the directory_line_edit.
        """
        directory = QFileDialog.getExistingDirectory(self, "Select an image folder")
        if directory:
            self.directory_line_edit.setText(directory)



    def toggle_scale_input(self):
        """
        Toggle visibility of scaling input fields based on the checkbox state.
        If unchecked, clears the scale_line_edit text.
        """
        checked = self.scale_check_box.isChecked()
        self.scale_line_edit.setVisible(checked)
        self.scale_label.setVisible(checked)
        if not checked:
            self.scale_line_edit.setText("")



    def convert_images(self):
        """
        Initiate image conversion based on user inputs.
        Collects necessary parameters, including directory, fps, resizing options, and output filename.
        Starts a new ConversionThread to handle the conversion and connects signals for success/error handling.
        Disables the convert button during the conversion.
        """
        try:
            directory = self.directory_line_edit.text()
            fps = int(self.fps_line_edit.text())
            resize_images = self.scale_check_box.isChecked()
            scale_width = int(self.scale_line_edit.text()) if (resize_images and self.scale_line_edit.text()) else None
            resize_mode = self.resize_mode_combo.currentText()

            filenames = sorted(os.listdir(directory))
            options = QFileDialog.Options()
            output_file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "GIF Files (*.gif);;All Files (*)", options=options)
            if not output_file_name:
                return

            if not output_file_name.endswith('.gif'):
                output_file_name += '.gif'

            self.convert_button.setEnabled(False)  # Disable the convert button

            self.conversion_thread = ConversionThread(directory, fps, resize_images, scale_width, resize_mode, output_file_name, filenames)
            self.conversion_thread.finished.connect(self.conversion_finished)
            self.conversion_thread.errorOccurred.connect(self.conversion_error)
            self.conversion_thread.start()

        except Exception as e:
            QMessageBox.critical(self, "ERROR", str(e))
            self.convert_button.setEnabled(True)



    def conversion_error(self, error_message):
        QMessageBox.critical(self, "ERROR :", error_message)
        self.convert_button.setEnabled(True)



    def conversion_finished(self):
        QMessageBox.information(self, "WIN", "Done !")
        self.convert_button.setEnabled(True) 


    def update_tooltip(self, index):
        tooltip_text = self.resize_mode_combo.itemData(index)
        self.resize_mode_combo.setToolTip(tooltip_text)


#____ ____ ____ ___  _  _ _ ____ ____ _       _  _ ____ ____ ____    _ _  _ ___ ____ ____ ____ ____ ____ ____ 
#| __ |__/ |__| |__] |__| | |    |__| |       |  | [__  |___ |__/    | |\ |  |  |___ |__/ |___ |__| |    |___ 
#|__] |  \ |  | |    |  | | |___ |  | |___    |__| ___] |___ |  \    | | \|  |  |___ |  \ |    |  | |___ |___ 
   

    def GUI(self):

        self.setWindowTitle("GIF maker")

        # Widgets
        self.directory_line_edit = QLineEdit()
        self.directory_line_edit.setPlaceholderText("Images folder")

        self.browse_button = QPushButton('Browse...')
        self.browse_button.clicked.connect(self.browse_directory)

        self.fps_label = QLabel("FPS:")
        self.fps_line_edit = QLineEdit()
        self.fps_line_edit.setPlaceholderText("images/s ")
        self.fps_line_edit.setToolTip("Less number will slow the GIF")


        self.scale_check_box = QCheckBox("Resize")
        self.scale_check_box.clicked.connect(self.toggle_scale_input)


        self.scale_label = QLabel("Échelle:")
        self.scale_line_edit = QLineEdit()
        self.scale_line_edit.setPlaceholderText("WIDTH")
        self.scale_line_edit.setToolTip("Height will ratio 👍")

        self.scale_line_edit.setVisible(False) 
        self.scale_label.setVisible(False)  


        self.resize_mode_label = QLabel("Method:")
        self.resize_mode_label.setToolTip("The method used for resizing the images in the GIF.")



        self.resize_mode_label = QLabel("Method:")
        self.resize_mode_combo = QComboBox()
        self.resize_mode_combo.addItems(["Nearest", "Bilinear", "Bicubic", "Antialias"])

        self.resize_mode_combo.setItemData(0, "Nearest: A fast resizing method that takes the nearest neighbor. Results in a more pixelated image.")
        self.resize_mode_combo.setItemData(1, "Bilinear: Uses linear interpolation between pixels. Results in a smoother image but may blur slightly.")
        self.resize_mode_combo.setItemData(2, "Bicubic: Uses cubic interpolation between pixels. Smoother than bilinear but slower.")
        self.resize_mode_combo.setItemData(3, "Antialias: A high-quality downsampling filter that minimizes artifacts and moiré patterns.")

        # Set the tooltip for the initial selection (Nearest)
        tooltip_text = self.resize_mode_combo.itemData(0)
        self.resize_mode_combo.setToolTip(tooltip_text)

        # Connect the tooltip update to the current index changed signal
        self.resize_mode_combo.currentIndexChanged.connect(self.update_tooltip)


        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_images)

        # Layouts
        self.mainLayout = QVBoxLayout()

        self.directory_layout = QHBoxLayout()
        self.directory_layout.addWidget(self.directory_line_edit)
        self.directory_layout.addWidget(self.browse_button)

        self.fps_layout = QHBoxLayout()
        self.fps_layout.addWidget(self.fps_label)
        self.fps_layout.addWidget(self.fps_line_edit)

        self.scale_layout = QHBoxLayout()
        self.scale_layout.addWidget(self.scale_check_box)
        self.scale_layout.addWidget(self.scale_label)
        self.scale_layout.addWidget(self.scale_line_edit)
        self.scale_layout.addWidget(self.resize_mode_label)
        self.scale_layout.addWidget(self.resize_mode_combo)

        self.mainLayout.addLayout(self.directory_layout)
        self.mainLayout.addLayout(self.fps_layout)
        self.mainLayout.addLayout(self.scale_layout)
        self.mainLayout.addWidget(self.convert_button)

        self.setLayout(self.mainLayout)


#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3


#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    main_window = gifMaker()
#    main_window.show()
#    sys.exit(app.exec_())
