from MediaManager.ui.components.logging_component import LoggingWindow


def test_given_new_logging_window_expect_title_and_default_message(qtbot):
    logging_window = LoggingWindow()

    qtbot.addWidget(logging_window)

    assert logging_window.windowTitle() == "Logs"
    assert logging_window._label.text() == "I'm floating on top!"


def test_given_logging_window_when_log_called_expect_label_updated(qtbot):
    logging_window = LoggingWindow()

    qtbot.addWidget(logging_window)

    logging_window.log("Something happened")

    assert logging_window._label.text() == "Something happened"
