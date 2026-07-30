from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
    ".heic",
}


def scan_images(folder_path: str) -> list[Path]:
    """Return all supported image files from a folder recursively."""

    folder = Path(folder_path)

    image_files = [
        file
        for file in folder.rglob("*")
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    return image_files