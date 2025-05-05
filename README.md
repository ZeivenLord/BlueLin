
# BlueLin — Video & Audio Downloader

**BlueLin** is a simple, user-friendly open-source tool for downloading YouTube and other supported videos or audio files as `.mp3` or `.mp4`.
It provides a clean graphical interface, requiring no technical knowledge or command line usage.

Developed by **Zeiven**.

---

## 🖥️ Features

✅ Download videos or audio from a single URL or a list of URLs (from a `.txt` file)  
✅ Choose format: `.mp3`, `.mp4`, or both  
✅ All downloads organized into separate folders (`/mp3` and `/mp4`)  
✅ Graphical interface with progress bar and log display  
✅ Portable — no installation required for end users (standalone `.exe`)  
✅ Logo and custom branding

---

## 📦 Download

If you only want to use the application **without installing Python or other tools:**

➡️ **[Download the executable (.exe)](link-to-your-release)** (Windows)

1. Download `BlueLin.exe`
2. Place it in any folder (the app will auto-create `/TéléchargementsVideos` subfolders)
3. Double-click to open
4. Paste a video link or select a `.txt` file with multiple links
5. Choose your format (.mp3, .mp4, or both)
6. Click **Download**

✅ Done! No need to install Python, ffmpeg, or any other dependency.

---

## 🛠️ Developers / Source Code

If you want to run or modify the source code:

### 📂 Project structure

```
/BlueLin/
 ├── main.py
 ├── logo.png
 ├── ffmpeg.exe
 ├── ffprobe.exe
 ├── ffplay.exe
 └── README.md
```

### ⚙️ Dependencies

- Python 3.8+
- Required packages:
    - `yt-dlp`
    - `pillow` (for logo handling)

Install them via:

```bash
pip install yt-dlp pillow
```

✅ `tkinter` is included in standard Python installations (no need to install manually).

---

## 🚀 Running the app from source

Simply run:

```bash
python main.py
```

👉 Make sure `ffmpeg.exe`, `ffprobe.exe`, and `ffplay.exe` are in the same folder as `main.py`.

---

## 🏗️ Building the executable (PyInstaller)

To compile your own standalone `.exe`:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Run this command:

```bash
pyinstaller --onefile --windowed --add-binary "ffmpeg.exe;." --add-binary "ffprobe.exe;." --add-binary "ffplay.exe;." --add-data "logo.png;." main.py
```

The executable will be in `/dist/main.exe`.

You can rename `main.exe` to `BlueLin.exe`.

✅ This `.exe` includes **Python, ffmpeg, ffprobe, ffplay, the logo, and all dependencies** — no external installation required.


## 🙌 Credits

Developed by **Zeiven**.

Thanks to the open-source projects:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/)
- [PyInstaller](https://pyinstaller.org/)
