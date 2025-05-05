
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

---

## 📦 Download executable

If you just want to use the app **without installing Python or dependencies:**

➡️ **[Download BlueLin.exe here](link-to-your-release-or-external-host)** (Windows)

1. Download `BlueLin.exe`
2. Place it in any folder
3. Double-click to open
4. Paste a video link or select a `.txt` file with multiple links
5. Choose format (.mp3, .mp4, or both)
6. Click **Download**

✅ Done! No need to install Python, ffmpeg, or other tools.

---

## 🛠️ Developers / Source Code

This repository only contains the **source code and assets**.  
⚠️ Due to file size limits, **compiled executables (`ffmpeg.exe`, `ffprobe.exe`, `ffplay.exe`) are NOT included.**

If you want to run the source code:

### 📂 Project structure

```
/BlueLin/
 ├── main.py
 ├── logo.png
 └── README.md
```

You must manually download the following binaries and place them in the same folder:

- `ffmpeg.exe`
- `ffprobe.exe`
- `ffplay.exe`

Download official builds from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) or use prebuilt versions from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/).

---

### ⚙️ Dependencies

- Python 3.8+
- Required packages:
    - `yt-dlp`
    - `pillow`

Install dependencies:

```bash
pip install yt-dlp pillow
```

✅ `tkinter` is included in standard Python installations.

---

## 🚀 Running the app from source

Simply run:

```bash
python main.py
```

👉 Make sure `ffmpeg.exe`, `ffprobe.exe`, and `ffplay.exe` are in the same folder as `main.py`.

---

## 🏗️ Building your own executable (PyInstaller)

If you want to create your own `.exe`:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Run:

```bash
pyinstaller --onefile --windowed --add-binary "ffmpeg.exe;." --add-binary "ffprobe.exe;." --add-binary "ffplay.exe;." --add-data "logo.png;." main.py
```

This will generate `main.exe` in the `/dist` folder.

You can rename `main.exe` to `BlueLin.exe`.

✅ The `.exe` will embed Python, ffmpeg, ffprobe, ffplay, the logo, and all dependencies.

⚠️ You cannot upload the `.exe` or ffmpeg binaries to this GitHub repository due to file size limits.

---

## 🙌 Credits

Developed by **Zeiven**.

Thanks to the open-source projects:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/)
- [PyInstaller](https://pyinstaller.org/)
