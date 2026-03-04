import os
import webbrowser
import datetime
import pyttsx3
import random
import wikipedia
import psutil

# -------------------- Text To Speech --------------------

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    """Speak and print text"""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# -------------------- Greeting --------------------

def greet():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning Sumer")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sumer")
    else:
        speak("Good Evening Sumer")

# -------------------- Utility Functions --------------------

def normalize_query(query):
    return query.lower().strip()

# -------------------- Spotify --------------------

def play_on_spotify(query):
    try:
        song_name = query.replace("play on spotify", "").strip()

        if song_name:
            speak(f"Playing {song_name} on Spotify")
            webbrowser.open(f"https://open.spotify.com/search/{song_name}")
        else:
            speak("Please tell me the song name")

    except Exception as e:
        speak("Unable to play the song")

# -------------------- Time --------------------

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {current_time}")

# -------------------- Date --------------------

def tell_date():
    today = datetime.date.today().strftime("%d %B %Y")
    speak(f"Today's date is {today}")

# -------------------- Open VS Code --------------------

def open_vscode():
    paths = [
        r"C:\Users\Haris\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        r"C:\Program Files\Microsoft VS Code\Code.exe"
    ]

    for path in paths:
        if os.path.exists(path):
            speak("Opening Visual Studio Code")
            os.startfile(path)
            return

    speak("Visual Studio Code not found on this system")

# -------------------- System Info --------------------

def system_info():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    speak(f"CPU usage is {cpu} percent")
    speak(f"Memory usage is {memory} percent")

# -------------------- Wikipedia --------------------

def search_wikipedia(query):
    try:
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(result)

    except Exception:
        speak("Sorry I could not find information")

# -------------------- Main Command Handler --------------------

def handle_command(query):

    query = normalize_query(query)

    if "time" in query:
        tell_time()

    elif "date" in query:
        tell_date()

    elif "open vscode" in query:
        open_vscode()

    elif "play on spotify" in query:
        play_on_spotify(query)

    elif "wikipedia" in query:
        search_wikipedia(query)

    elif "system status" in query:
        system_info()

    elif "exit" in query:
        speak("Goodbye Sumer")
        exit()

    else:
        speak("Sorry I did not understand")

# -------------------- Main Program --------------------

if __name__ == "__main__":

    greet()

    while True:
        query = input("Enter command: ")
        handle_command(query)
