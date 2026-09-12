from PySide6.QtWidgets import QMainWindow

from MediaManager.ui.components.logging_component import LoggingWindow
from MediaManager.ui.views.home_view import HomeView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Media Manager")

        # Add log to main window
        # logging_window = LoggingWindow()
        self.home_view = HomeView()

        self.setCentralWidget(self.home_view)
