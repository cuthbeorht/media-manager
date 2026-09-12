from MediaManager.ui.main_window import MainWindow


def test_app_startup(qtbot):
    # Instantiate the main window widget
    app_window = MainWindow()

    # Add widget to qtbot to handle cleanup and events
    qtbot.addWidget(app_window)

    # Show the window (optional, depends on testing needs)
    app_window.show()

    # Assert that the app initialized successfully
    assert app_window.isVisible()
