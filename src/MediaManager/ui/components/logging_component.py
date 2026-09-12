from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt


class LoggingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logs")
        self.resize(400, 250)

        self.setWindowFlags(Qt.Window | Qt.Tool | Qt.WindowStaysOnTopHint)

        self._label = QLabel("I'm floating on top!", self)
        self._label.setAlignment(Qt.AlignCenter)

    def log(self, message: str):
        self._label.setText(message)
