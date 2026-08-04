# from pathlib import Path
# from models.image import Image

# SUPPORTED_EXTENSIONS = {
#     ".jpg",
#     ".jpeg",
#     ".png",
#     ".bmp",
#     ".webp",
#     ".heic",
# }


# def scan_images(folder_path: str) -> list[Path]:
#     """Return all supported image files from a folder recursively."""

#     folder = Path(folder_path)

#     image_files = [
#         file
#         for file in folder.rglob("*")
#         if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS
#     ]

#     return image_files

from pathlib import Path

from src.models.image import Image

from src.services.metadata import extract_metadata


SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
    ".heic",
}


def scan_images(folder_path: str) -> list[Image]:
    folder = Path(folder_path)

    images = []

    for file in folder.rglob("*"):
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
            metadata = extract_metadata(file)

            image = Image(
                path=file,
                filename=file.name,
                extension=file.suffix.lower(),
                size=metadata["size"],
                width=metadata["width"],
                height=metadata["height"],
            )
            # image = Image(
            #     path=file,
            #     filename=file.name,
            #     extension=file.suffix.lower(),
            #     size=0,
            #     width=0,
            #     height=0,
            # )

            images.append(image)

    return images