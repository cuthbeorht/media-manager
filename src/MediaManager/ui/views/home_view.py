from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget

from MediaManager.ui.components.library_component import LibraryComponent


class HomeView(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()

        self.library_component = LibraryComponent()
        self._add_item_button = QPushButton("Add item", self)
        self._add_item_button.clicked.connect(self.handle_add_button_event)

        self._layout.addWidget(self.library_component)
        self._layout.addWidget(self._add_item_button)

        self.setLayout(self._layout)

    def handle_add_button_event(self):
        self.library_component.add_library_item("foo")
