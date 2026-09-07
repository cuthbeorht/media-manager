from MediaManager import MyWidget
from PySide6.QtCore import Qt

def test_click_me_button(qtbot):
    window = MyWidget()

    qtbot.addWidget(window)

    assert window.text.text() == "Hello World"

    qtbot.mouseClick(window.button, Qt.MouseButton.LeftButton)

    assert window.button.text() == "Click me!"