# Nova Voice Assistant

**Nova** is a Python-based desktop voice assistant that responds to natural speech commands and automates tasks such as opening websites, playing music, controlling system volume, fetching weather updates, and more.

---

## 🚀 Features

- **Voice Command Recognition** using `speech_recognition`
- **Text-to-Speech Responses** using `pyttsx3`
- **Weather Updates** via OpenWeatherMap API
- **News Headlines** via NewsAPI
- **Google & Wikipedia Search** via `wikipedia` and web scraping
- **YouTube Search & Playback** through browser automation
- **Play Local Songs** using predefined YouTube links
- **System Volume Controls** using `nircmd.exe`
- **Open System Folders** like Downloads, Documents, etc.
- **Shutdown System** via voice command

---

## 🛠️ Tech Stack

- Python 3.x
- `speech_recognition`
- `pyttsx3`
- `requests`
- `wikipedia`
- `pywhatkit`
- Built-in modules: `webbrowser`, `os`, `re`

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
````

Or install manually:

```bash
pip install pyttsx3 SpeechRecognition requests wikipedia pywhatkit
```

---

## 🔐 API Keys Required

This project uses external APIs:

### 1. OpenWeatherMap

* Sign up at [openweathermap.org](https://openweathermap.org/)
* Get your API key
* Add it as an environment variable:

```powershell
$env:OPEN_WEATHER="your_api_key_here"
```

### 2. NewsAPI

* Sign up at [newsapi.org](https://newsapi.org/)
* Replace the placeholder in `main.py`:

```python
newsapi = "your_news_api_key_here"
```

---

## ⚠️ Important: `nircmd.exe`

To enable volume control (up/down/mute) and shutdown functionality:

* Download [`nircmd.exe`](https://www.nirsoft.net/utils/nircmd.html)
* Place it in the same directory as your Python files (`NovaVoiceAssistant/`)

> Without this file, volume and shutdown features will not work.

---

## 🧪 How to Run

```bash
python main.py
```

When prompted, say the wake word: **"Nova"**

Then use voice commands like:

* `"Open Google"`
* `"Search YouTube for best coding music"`
* `"Play believer"`
* `"Weather Delhi"`
* `"News"`
* `"Shutdown"`
* `"Open downloads folder"`

---

## 📁 Project Structure

```
NovaVoiceAssistant/
├── main.py
├── sysop.py
├── search.py
├── musiclibrary.py
├── weather.py
├── nircmd.exe
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🙌 Credits

Built by **Sanjay** as part of a portfolio project and a way to explore Python automation.

> Feel free to fork, modify, and contribute to this project.
