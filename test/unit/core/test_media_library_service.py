from pathlib import Path

import pytest

from MediaManager.core.media import MediaLibraryService


@pytest.fixture
def songs_in_fixtures(project_root: str) -> int:
    counter = 0
    media_path = Path(f"{project_root}/test/fixtures/media")

    for item in media_path.iterdir():
        counter += 1

    return counter


@pytest.fixture
def media_root(project_root: str) -> Path:
    return Path(f"{project_root}/test/fixtures/media")


def test_given_valid_path_with_music_walk_expect_valid_number_of_files(
    media_root: Path, songs_in_fixtures: int
):

    service = MediaLibraryService(media_root)

    service.walk()

    assert len(service.media_files) == songs_in_fixtures


def test_given_valid_path_with_music_walk_expect_valid_media_file_data(
    media_root: Path, songs_in_fixtures: int
):

    service = MediaLibraryService(media_root)

    service.walk()

    assert service.media_files[0].type == "MP3"
    assert service.media_files[0].size == 3678720
    assert (
        "test/fixtures/media/desifreemusic-creative-commons-music-free-download-and-safe-for-monetization-364593.mp3"
        in str(service.media_files[0].full_file_name)
    )
