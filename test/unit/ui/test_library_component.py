from MediaManager.ui.components.library_component import LibraryComponent


def test_given_new_library_component_expect_default_item(qtbot):
    library_component = LibraryComponent()

    qtbot.addWidget(library_component)

    assert library_component._list_box.count() == 1
    assert library_component._list_box.item(0).text() == "Foo"


def test_given_library_component_when_add_library_item_expect_item_appended(qtbot):
    library_component = LibraryComponent()

    qtbot.addWidget(library_component)

    library_component.add_library_item("Bar")

    assert library_component._list_box.count() == 2
    assert library_component._list_box.item(1).text() == "Bar"
