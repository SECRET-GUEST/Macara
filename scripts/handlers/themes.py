from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,pyqtSignal,QSize

from functools import partial


# Theme configuration
class ThemeSelector(QDialog):

    theme_selected = pyqtSignal(int)  # signal to refresh themes on title bar

    def __init__(self, parent=None, logger=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon())
        
        self.logger = logger
        self.selected_theme = None

        self.setWindowTitle("Themes")

        # Hide context help button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowIcon(QIcon(self.logger.ressource_path("assets/ico/macara.png")))

        self.init_ui()


    def on_theme_button_clicked(self, theme_id):
        self.selected_theme = theme_id
        self.theme_selected.emit(theme_id)
        self.accept()


    def init_ui(self):
        # Fisrt we make a vertical grid
        layout = QVBoxLayout()

        # Add buttons for each theme
        for i in range(1, 6):
            # Create a horizontal layout for the theme row
            theme_layout = QHBoxLayout()

            # Add an image button for the theme
            theme_button = QPushButton(self)
            image_path = self.logger.ressource_path(f"assets/ico/theme{i}.png")
            theme_button.setIcon(QIcon(image_path))
            theme_button.setIconSize(QSize(108, 108))
            theme_button.clicked.connect(partial(self.on_theme_button_clicked, i))
            theme_layout.addWidget(theme_button)

            # Add the theme row layout to the dialog layout
            layout.addLayout(theme_layout)

        # Set the dialog layout
        self.setLayout(layout)

