from src.scanner import scan_images


def main():
    print("=" * 50)
    print("📸 PhotoOrganizer")
    print("Version 1.0")
    print("=" * 50)

    folder = input("\nEnter folder path: ")

    images = scan_images(folder)

    print(f"\nFound {len(images)} images.\n")

    for image in images:
        print(image)


if __name__ == "__main__":
    main()