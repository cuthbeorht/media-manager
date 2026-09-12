from PySide6.QtWidgets import QVBoxLayout, QWidget, QTextEdit

class LibraryComponent(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()
        
        self._textbox = QTextEdit(self)
        self._textbox.setText("fpoo")

        self._layout.addWidget(self._textbox)

        self.setLayout(self._layout)