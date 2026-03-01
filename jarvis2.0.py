import os
import sys
import webbrowser
import datetime
import logging
import random
import wikipedia
import psutil
import pyautogui
import pyttsx3

# -------------------- Text To Speech --------------------

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

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

def play_on_spotify(query):
    song_name = query.replace("play on spotify", "").strip()
    if song_name:
        speak(f"Playing {song_name} on Spotify")
        webbrowser.open(f"https://open.spotify.com/search/{song_name}")
    else:
        speak("Please tell me the song name.")

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {current_time}")

def tell_date():
    today = datetime.date.today().strftime("%d %B %Y")
    speak(f"Today's date is {today}")

def open_vscode():
    possible_paths = [
        r"C:\Users\Haris\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        r"C:\Program Files\Microsoft VS Code\Code.exe"
    ]

    for path in possible_paths:
        if os.path.exists(path):
            speak("Opening Visual Studio Code")
            os.startfile(path)
            return

    speak("VS Code not found on this system.")

def restart_system():
    speak("Restarting the system in 5 seconds")
    os.system("shutdown /r /t 5")

def shutdown_system():
    speak("Shutting down the system in 5 seconds")
    os.system("shutdown /s /t 5")

def search_google(query):
    search_term = query.replace("search", "").strip()
    if search_term:
        speak(f"Searching {search_term} on Google")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
    else:
        speak("What should I search?")

def search_youtube(query):
    search_term = query.replace("youtube", "").strip()
    if search_term:
        speak(f"Searching {search_term} on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")
    else:
        speak("What should I search on YouTube?")

def wikipedia_search(query):
    topic = query.replace("wikipedia", "").strip()
    try:
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)
    except:
        speak("Sorry, I couldn't find information on that topic.")

def open_website(query):
    site = query.replace("open", "").strip()
    if site:
        speak(f"Opening {site}")
        webbrowser.open(f"https://{site}.com")
    else:
        speak("Which website should I open?")

def battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"Battery is at {percent} percent")
    else:
        speak("Unable to fetch battery status")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    screenshot.save(filename)
    speak("Screenshot taken and saved.")

def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I told my computer I needed a break. It said no problem and froze.",
        "Debugging is like being a detective in a crime movie where you are also the murderer."
    ]
    speak(random.choice(jokes))

# -------------------- Command Handler --------------------

def handle_query(query):
    try:
        query = normalize_query(query)

        if "play on spotify" in query:
            play_on_spotify(query)

        elif "time" in query:
            tell_time()

        elif "date" in query:
            tell_date()

        elif "open code" in query:
            open_vscode()

        elif "restart system" in query:
            restart_system()

        elif "shutdown system" in query:
            shutdown_system()

        elif "search" in query:
            search_google(query)

        elif "youtube" in query:
            search_youtube(query)

        elif "wikipedia" in query:
            wikipedia_search(query)

        elif "battery" in query:
            battery_status()

        elif "screenshot" in query:
            take_screenshot()

        elif "joke" in query:
            tell_joke()

        elif "open" in query:
            open_website(query)

        else:
            speak("Sorry, I did not understand the command.")

    except Exception as e:
        speak("Something went wrong")
        logging.error(f"Error: {str(e)}")

# -------------------- Run Loop --------------------

if __name__ == "__main__":
    greet()
    
    while True:
        query = input("Enter Command: ")

        if normalize_query(query) == "exit":
            speak("Goodbye Sumer")
            sys.exit()

        handle_query(query)
