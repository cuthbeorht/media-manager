from pathlib import Path
from typing import Self
import os

from pydantic import BaseModel


class MediaFile(BaseModel):
    full_file_name: Path
    size: int
    length: int
    type: str

    @classmethod
    def from_file(cls, path: str) -> Self:

        media_file = Path(path)
        # make sure file exists
        if not media_file.is_file():
            raise ValueError(f"File {path} does not exist.")

        file_size = media_file.stat().st_size

        return cls(full_file_name=media_file, size=file_size, length=200, type="MP3")


class MediaMetadata(BaseModel):
    title: str
    artist: str
    album: str


class MediaLibraryService:
    def __init__(self, root_dir: Path):
        self._root_dir = root_dir
        self._media_files: list[MediaFile] = []

    def walk(self):
        for root, dirs, files in os.walk(self._root_dir):
            for filename in files:
                full_path = os.path.join(root, filename)
                self._media_files.append(MediaFile.from_file(full_path))

    @property
    def media_files(self) -> list[MediaFile]:
        return self._media_files

