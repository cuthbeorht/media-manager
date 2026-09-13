from pathlib import Path

from MediaManager.core.media import MediaFile


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


def test_given_valid_mp3_file_to_media_file_expect_valid_media_file(project_root: str):
    media_file_path = f"{project_root}/test/fixtures/media/desifreemusic-creative-commons-music-free-download-and-safe-for-monetization-364593.mp3"

    expected_media_file = MediaFile(
        full_file_name=Path(
            f"{project_root}/test/fixtures/media/desifreemusic-creative-commons-music-free-download-and-safe-for-monetization-364593.mp3"
        ),
        size=3678720,
        length=200,
        type="MP3",
    )

    actual_media_file = MediaFile.from_file(media_file_path)

    assert expected_media_file == actual_media_file
