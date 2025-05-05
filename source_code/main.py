import yt_dlp
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from threading import Thread
from PIL import Image, ImageTk
import sys

def resource_path(relative_path):
    """Permet de trouver les fichiers même après avoir généré l'exe avec PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MyLogger:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def debug(self, msg):
        self.text_widget.insert(tk.END, msg + '\n')
        self.text_widget.see(tk.END)

    def warning(self, msg):
        self.debug("[WARNING] " + msg)

    def error(self, msg):
        self.debug("[ERROR] " + msg)

def download_audio_as_mp3(youtube_url, output_path, ffmpeg_path, logger):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path,
        'logger': logger,
        'progress_hooks': [progress_hook],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def download_video_as_mp4(youtube_url, output_path, ffmpeg_path, logger):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'ffmpeg_location': ffmpeg_path,
        'logger': logger,
        'progress_hooks': [progress_hook],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip().replace('%', '')
        try:
            progress_var.set(float(percent))
        except:
            pass
    elif d['status'] == 'finished':
        progress_var.set(100)

def process_links(links, choice, base_output_path, ffmpeg_path, logger):
    mp3_folder = os.path.join(base_output_path, "mp3")
    mp4_folder = os.path.join(base_output_path, "mp4")

    for link in links:
        logger.debug(f"Téléchargement en cours : {link}")
        if choice == 'mp3':
            download_audio_as_mp3(link, mp3_folder, ffmpeg_path, logger)
        elif choice == 'mp4':
            download_video_as_mp4(link, mp4_folder, ffmpeg_path, logger)
        elif choice == 'both':
            download_audio_as_mp3(link, mp3_folder, ffmpeg_path, logger)
            download_video_as_mp4(link, mp4_folder, ffmpeg_path, logger)

    messagebox.showinfo("Téléchargement terminé", "Tous les téléchargements sont terminés !")

def start_download():
    links = []
    if link_entry.get():
        links.append(link_entry.get().strip())
    elif file_path.get():
        try:
            with open(file_path.get(), 'r', encoding='utf-8') as f:
                links = [line.strip() for line in f if line.strip()]
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lire le fichier : {e}")
            return
    else:
        messagebox.showwarning("Aucun lien", "Veuillez entrer un lien ou sélectionner un fichier de liens.")
        return

    progress_var.set(0)
    logger = MyLogger(log_text)

    def thread_task():
        process_links(links, format_choice.get(), output_folder, ffmpeg_exe_path, logger)

    Thread(target=thread_task).start()

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if filepath:
        file_path.set(filepath)

# Chemins
ffmpeg_exe_path = resource_path("ffmpeg.exe")  # ✅ utilisation de resource_path() pour PyInstaller
output_folder = os.path.join(os.getcwd(), "TéléchargementsVideos")
os.makedirs(output_folder, exist_ok=True)

# Interface
root = tk.Tk()
root.title("BlueLin - Zeiven")
root.geometry("600x500")

# Charger le logo comme icône de fenêtre
try:
    logo_path = resource_path("logo.png")
    original_icon = Image.open(logo_path)
    resized_icon = original_icon.resize((32, 32))
    icon_img = ImageTk.PhotoImage(resized_icon)
    root.iconphoto(False, icon_img)
except Exception as e:
    print(f"Aucun logo trouvé ou problème de chargement : {e}")

# Widgets
tk.Label(root, text="Lien vidéo :").pack()
link_entry = tk.Entry(root, width=60)
link_entry.pack()

tk.Label(root, text="OU sélectionnez un fichier de liens (.txt) :").pack()
file_path = tk.StringVar()
file_entry = tk.Entry(root, textvariable=file_path, width=50)
file_entry.pack(side=tk.LEFT, padx=5)
browse_button = tk.Button(root, text="Parcourir", command=browse_file)
browse_button.pack(side=tk.LEFT)

tk.Label(root, text="Format de téléchargement :").pack(pady=10)
format_choice = tk.StringVar(value='mp3')
tk.Radiobutton(root, text="Audio (.mp3)", variable=format_choice, value='mp3').pack()
tk.Radiobutton(root, text="Vidéo (.mp4)", variable=format_choice, value='mp4').pack()
tk.Radiobutton(root, text="Les deux", variable=format_choice, value='both').pack()

download_button = tk.Button(root, text="Télécharger", command=start_download)
download_button.pack(pady=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill=tk.X, padx=10, pady=5)

log_text = tk.Text(root, height=10, width=70)
log_text.pack(padx=10, pady=10)

tk.Label(root, text="Développé par Zeiven", font=("Arial", 10, "italic")).pack(side=tk.BOTTOM, pady=5)

root.mainloop()
