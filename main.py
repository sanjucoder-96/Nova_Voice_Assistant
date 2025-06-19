import speech_recognition as sr
import pyttsx3 #python text to speech
import sysop
import sys
import webbrowser
import requests
import musiclibrary
import time 
import search
import weather
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index as needed
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)
def speak(text):
    engine.say(text)
    engine.runAndWait()
newsapi = "a0787f8dd0ec497cb52cd010493be1b4"

def process_command(c):
    print(f"Processing: {c}")
    c_lower = c.lower()

    if "open google" in c_lower:
        webbrowser.open("https://google.com")
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
    elif "stop listening" in c_lower:
        speak("Goodbye sir.")
        sys.exit()
    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c_lower:
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c_lower:
        webbrowser.open("https://spotify.com")
    elif c_lower.startswith("play"):
        song = " ".join(c.split(" ")[1:]).strip() # play wolf dsnfkldsf
        link = musiclibrary.music.get(song.lower())
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")
    elif "news" in c_lower:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for i, article in enumerate(articles[:10], 1):
                speak(f"{i}. {article['title']}")
        else:
            print(f"Error fetching news: {r.status_code}")
    elif c_lower.startswith("search youtube for") or c_lower.startswith("youtube for"):
        if c_lower.startswith("search youtube for"):
            query = " ".join(c.split(" ")[3:]).strip()
        else:
            query = " ".join(c.split(" ")[2:]).strip()
        result = search.search_youtube(query)
        print(result)
        speak(result)

    elif "weather" in c.lower() or "whether" in c.lower():
        city = c.lower().replace("weather", "").strip()
        if city:
            weather_report = weather.get_weather_update(city)
            speak(weather_report)
        else:
            speak("Please tell me the city name for the weather report.")


    elif c_lower.startswith("google for") or c_lower.startswith("search"):
        query = " ".join(c.split(" ")[2:]).strip()
        result = search.search_google(query)
        print(result)
        speak(result)
    elif "increase volume" in c.lower():
        sysop.volume_up()
        speak("Volume increased.")
    elif "shutdown" in c.lower():
        speak("Shutting down the system.")
        sysop.shutdown()
    elif "decrease volume" in c_lower or "volume down" in c_lower:
        sysop.volume_down()
        speak("Volume decreased.")

    elif "mute" in c_lower and "volume" in c_lower:
        sysop.mute_volume()
        speak("Volume muted.")
    
    elif "open" in c_lower and "folder" in c_lower:
        folder_name = c_lower.replace("open", "").replace("folder", "").strip()
        response = sysop.open_folder_by_name(folder_name)
        speak(response)
    else:
        speak("I'm not sure how to handle that command.")

if __name__ == "__main__": 
    recognizer = sr.Recognizer()
    speak("Initialising Nova")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Say wake word 'Nova'")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}") #NOVA.lower()->nova
                if "nova" in text.lower():
                    speak("Yes sir, I'm here.")
                    break
        except Exception as e:
            print(f"Error listening for wake word: {e}")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for command...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
                command = recognizer.recognize_google(audio)
                print(f"Command heard: {command}")
                process_command(command)
                time.sleep(1)
        except sr.UnknownValueError:
            print("Could not understand command, please repeat.")
        except Exception as e:
            print(f"Error listening for command: {e}")
