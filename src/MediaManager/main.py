import sys

import PySide6.QtCore
from PySide6 import QtWidgets

from MediaManager.ui.main_window import MainWindow


def main() -> None:
    print("Hello from media-manager!")

    print(PySide6.__version__)
    print(PySide6.QtCore.__version__)

    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
