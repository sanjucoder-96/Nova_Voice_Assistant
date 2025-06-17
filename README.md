Nova Voice Assistant

Nova is a Python-based desktop voice assistant that responds to natural speech commands and automates tasks such as opening websites, playing music, controlling system volume, fetching weather updates, and more.

🚀 Features

Voice Command Recognition using speech_recognition

Text-to-Speech Responses using pyttsx3

Weather Updates using OpenWeatherMap API

News Headlines using NewsAPI

Google & Wikipedia Search via wikipedia and web scraping

YouTube Search & Playback via browser automation

Play Local  Songs using predefined YouTube links

System Volume Controls via nircmd.exe

Open System Folders like Downloads, Documents, etc.

Shutdown System with voice command

🛠️ Tech Stack

Python 3.x

speech_recognition

pyttsx3

requests

wikipedia

pywhatkit

webbrowser, os, re

📦 Requirements

Install dependencies with:

pip install -r requirements.txt

Or install manually:

pip install pyttsx3 SpeechRecognition requests wikipedia pywhatkit

🔐 API Keys Required

This project uses external APIs:

1. OpenWeatherMap

Sign up at https://openweathermap.org/

Get your API key

Add it as an environment variable:

Windows PowerShell:

$env:OPEN_WEATHER="your_api_key_here"

2. NewsAPI

Sign up at https://newsapi.org/

Replace the placeholder key in main.py with your API key:

newsapi = "your_news_api_key_here"

⚠️ Important: nircmd.exe

To enable system volume control (volume up/down/mute), download and place nircmd.exe in the same directory as your Python files (NovaVoiceAssistant/).

Without this, volume and shutdown features won't work.

🧪 How to Run

python main.py

Speak the wake word: Nova

Then say commands like:

"Open Google"

"Search YouTube for best coding music"

"Play rowdy"

"Weather Delhi"

"News"

"Shutdown"

"Open downloads folder"

📁 Project Structure

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

🤖 Credits

Built by Sanjay as part of a portfolio project and Exploring Python.

Feel free to fork, modify, and contribute to this project.

