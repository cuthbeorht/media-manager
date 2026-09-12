from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QWidget

from MediaManager.ui.components.library_component import LibraryComponent

class HomeView(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()                

        library_component = LibraryComponent()

        self._layout.addWidget(library_component)

        self.setLayout(self._layout)


        

