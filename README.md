# 📸 MemoryOffice

MemoryOffice is an offline Python application designed to intelligently organize, search, and manage personal photos and videos.

The goal of this project is to provide a fast, privacy-focused media management solution that runs entirely on your local machine without uploading your files to the cloud.

---

## ✨ Features

### Current

- Recursive folder scanning
- Image discovery
- Support for multiple image formats
- Offline processing
- Clean and modular architecture

### Planned

- Face Detection
- Face Recognition
- Duplicate Photo Detection
- Similar Image Search
- Video Organization
- Metadata Indexing
- Fast Local Search
- Smart Albums
- EXIF Metadata Viewer
- Desktop GUI
- AI-powered photo categorization

---

## 📂 Project Structure

```
MemoryOffice/
│
├── src/                 # Source code
├── data/                # Local testing data (ignored by Git)
├── database/            # SQLite database
├── logs/                # Application logs
├── models/              # ML models
├── output/              # Generated output
├── tests/               # Unit tests
│
├── main.py              # Entry point
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

---

## 🖼 Supported Image Formats

- JPG
- JPEG
- PNG
- BMP
- WEBP
- HEIC

More formats will be added in future releases.

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Rahul03-bpositive/MO-MemoryOffice.git
```

Move into the project

```bash
cd MO-MemoryOffice
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## 🛠 Technologies Used

- Python 3.13
- OpenCV
- Pillow
- Pillow-HEIF
- NumPy
- pathlib

---

## 🎯 Project Goals

MemoryOffice aims to become a complete offline media management solution capable of:

- Organizing thousands of photos
- Recognizing people using face recognition
- Finding duplicate images
- Searching photos instantly
- Managing videos
- Preserving user privacy by processing everything locally

---

## 🛣 Roadmap

- [x] Project setup
- [x] Image scanner
- [ ] Metadata extraction
- [ ] SQLite integration
- [ ] Face detection
- [ ] Face recognition
- [ ] Duplicate detection
- [ ] Video scanner
- [ ] Search engine
- [ ] Desktop GUI

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

If you'd like to contribute, feel free to open an issue or submit a pull request.

---

## 📄 License

This project will be released under the MIT License.

---

## 👨‍💻 Author

**Rahul Gupta**

GitHub: https://github.com/Rahul03-bpositive
