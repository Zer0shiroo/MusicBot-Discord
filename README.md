


# 🎵 Discord Music Bot

A simple and functional Discord music bot built with `discord.py` and `yt_dlp`.

This bot can play music in voice channels from YouTube using the `@play` command. It also supports pause, resume, and stop functionalities, with a touch of style.

---

## ✅ Features

- 🔎 Play songs using `@play <song name or YouTube URL>`
- ⏸️ Pause and ▶️ resume music
- ⏹️ Stop music and disconnect from the voice channel
- 🎧 Automatically joins the user’s voice channel
- 🎶 Displays the song title being played
- Custom bot status and presence

---

## ⚙️ Requirements

- Python 3.8+
- FFmpeg installed and accessible (see below)
- Discord Bot Token (from [Discord Developer Portal](https://discord.com/developers/applications))

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/music-bot.git
cd music-bot
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up your `.env` file**

Create a `.env` file in the root of the project with:

```
DISCORD_TOKEN=your_token_here
FFMPEG_PATH=C:\\ffmpeg\\bin\\ffmpeg.exe
```

> Make sure the `FFMPEG_PATH` matches the location of your `ffmpeg.exe`. You can download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

4. **Run the bot**

```bash
python bot.py
```

---

## 💬 Bot Commands

| Command   | Description                               |
| --------- | ----------------------------------------- |
| `@play`   | Play a song by name or YouTube URL        |
| `@pause`  | Pause the current song                    |
| `@resume` | Resume the paused song                    |
| `@stop`   | Stop the song and disconnect from channel |

---

## 🔐 Security Tip

Make sure your `.env` file is in your `.gitignore` so your token is never exposed.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👑 Bot Presence

> "🎧 Soy el MVP del sonido. Si vas a poner música, que sea con clase. Déjamelo a mí.🎵"

---

Enjoy your music!
