from dataclasses import dataclass
from pathlib import Path


@dataclass
class Image:
    path: Path
    filename: str
    extension: str
    size: int
    width: int
    height: int