from PySide6.QtWidgets import QListWidget, QVBoxLayout, QWidget, QTextEdit

class LibraryComponent(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()
        
        self._list_box = QListWidget()
        self._list_box.addItems(["Foo"])

        self._layout.addWidget(self._list_box)

        self.setLayout(self._layout)