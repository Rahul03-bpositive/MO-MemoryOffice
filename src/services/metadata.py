from pathlib import Path
from pillow_heif import register_heif_opener
from PIL import Image as PILImage
register_heif_opener()




def extract_metadata(image_path: Path) -> dict:
    """
    Extract basic metadata from an image.
    """

    with PILImage.open(image_path) as img:
        width, height = img.size

    return {
        "size": image_path.stat().st_size,
        "width": width,
        "height": height,
        "format": img.format,
    }