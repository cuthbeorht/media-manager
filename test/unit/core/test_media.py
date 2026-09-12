from pathlib import Path

from MediaManager.core.media import MediaFile, MediaMetadata


def test_given_valid_media_file_data_create_mediafile_expect_valid_mediafile():
    expected_media_file = MediaFile(
        full_file_name=Path("/tmp/potato"), size=9999, length=180, type="MP3"
    )

    actual_media_file = MediaFile(
        full_file_name=Path("/tmp/potato"), size=9999, length=180, type="MP3"
    )

    assert expected_media_file == actual_media_file


def test_given_differnet_media_file_data_create_mediafile_expect_different_mediafile():
    expected_media_file = MediaFile(
        full_file_name=Path("/tmp/potato/fries"), size=9999, length=180, type="MP3"
    )

    actual_media_file = MediaFile(
        full_file_name=Path("/tmp/potato"), size=9999, length=180, type="MP3"
    )

    assert expected_media_file != actual_media_file


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
