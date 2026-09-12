from pathlib import Path

from pydantic import BaseModel


class MediaFile(BaseModel):
    full_file_name: Path
    size: int
    length: int
    type: str


class MediaMetadata(BaseModel):
    title: str
    artist: str
    album: str


class MediaLibraryService:
    def __init__(self, root_dir: Path):
        self._root_dir = root_dir

    def walk(self):
        pass
