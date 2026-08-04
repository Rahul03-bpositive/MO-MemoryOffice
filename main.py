from src.services.scanner import scan_images


def main():
    print("=" * 50)
    print("📸 PhotoOrganizer")
    print("Version 1.0")
    print("=" * 50)

    folder = input("\nEnter folder path: ")

    images = scan_images(folder)

    print(f"\nFound {len(images)} images.\n")

    for image in images:
        print(f"Filename : {image.filename}")
        print(f"Extension: {image.extension}")
        print(f"Size     : {image.size} bytes")
        print(f"Width    : {image.width}")
        print(f"Height   : {image.height}")
        print("-" * 40)


if __name__ == "__main__":
    main()