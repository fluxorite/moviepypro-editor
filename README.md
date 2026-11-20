<div align="center">

# 🎬 MoviePy Pro

**A terminal-based video editor built on MoviePy.**
Pick an operation from an interactive menu and edit your video without writing any code.


Engineered by **HANSRAJ**

</div>

---

## ✨ Features

| # | Operation | What it does |
|---|-----------|--------------|
| 1 | **Trim Video** | Cut the video to a chosen start and end time |
| 2 | **Change Speed** | Speed the video up or slow it down |
| 3 | **Resize Resolution** | Change the video width and height |
| 4 | **Rotate/Flip** | Rotate the video or flip it horizontally/vertically |
| 5 | **Mute Audio** | Remove the audio track from the video |
| 6 | **Volume Control** | Increase or decrease the audio volume |
| 7 | **Brightness/Color** | Adjust the brightness and color of the video |
| 8 | **Fade In/Out** | Add fade-in and fade-out effects |
| 9 | **Reverse Video** | Play the video backwards |
| 10 | **Mirror Effect** | Create a mirrored version of the video |
| 11 | **Crop Video** | Crop the video frame to a selected area |
| 12 | **Invert Color** | Invert the colors of the video |
| 13 | **Extract MP3** | Save the audio of the video as an MP3 file |
| 14 | **Change Background Music** | Replace the video's audio with another music file |
| 15 | **Exit** | Close the script |

---

## 📦 Requirements

- Python 3
- MoviePy
- FFmpeg
- gum (for the interactive menu)
- toilet and boxes (for the ASCII art header)

---

## ⚙️ Installation

### 📱 Termux

```bash
pkg install python ffmpeg toilet boxes gum
pip install moviepy
```

### 🐧 Debian / Ubuntu

```bash
sudo apt install python3 python3-pip ffmpeg toilet boxes
pip install moviepy
```

---

## 🚀 Usage

```bash
python moviepypro.py
```

Enter the input video filename when asked, then choose an operation with the arrow keys and press Enter.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
