from MediaManager.core.media import MediaMetadata


def test_given_valid_metadata_create_mediametadata_expect_valid_mediametdata():
    expected_metadata = MediaMetadata(
        title="Cool title", artist="The bestest artist ever", album="Some awesome album"
    )

    actual_metadata = MediaMetadata(
        title="Cool title", artist="The bestest artist ever", album="Some awesome album"
    )

    assert expected_metadata == actual_metadata


def test_given_differnet_metadata_create_mediametadata_expect_different_mediametdata():
    expected_metadata = MediaMetadata(
        title="Cool different title",
        artist="The bestest artist ever",
        album="Some awesome album",
    )

    actual_metadata = MediaMetadata(
        title="Cool title", artist="The bestest artist ever", album="Some awesome album"
    )

    assert expected_metadata != actual_metadata
