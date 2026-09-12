from PySide6.QtCore import Qt

from MediaManager import MainWindow


def test_click_me_button(qtbot):
    window = MainWindow()

    qtbot.addWidget(window)

    assert window.windowTitle() == "Media Manager"


def test_given_app_normal_start_init_main_window_expect_add_item_button(qtbot):

    window = MainWindow()
    add_item_button = window.home_view._add_item_button

    qtbot.mouseClick(add_item_button, Qt.MouseButton.LeftButton)

    assert add_item_button.text() == "Add Item"
