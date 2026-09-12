from pathlib import Path
from typing import Self

from pydantic import BaseModel


class MediaFile(BaseModel):
    full_file_name: Path
    size: int
    length: int
    type: str

    @classmethod
    def from_file(cls, path: str) -> Self:
        return cls(full_file_name=Path(path), size=9999, length=200, type="MP3")


class MediaMetadata(BaseModel):
    title: str
    artist: str
    album: str


class MediaLibraryService:
    def __init__(self, root_dir: Path):
        self._root_dir = root_dir

    def walk(self):
        pass
