import os
import webbrowser
import datetime
import random
import logging
import pyttsx3
import sys

# -------------------- Voice Engine Setup --------------------
engine = pyttsx3.init()

def setup_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index for female voice
    engine.setProperty('rate', 170)  # Speed
    engine.setProperty('volume', 1)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

setup_voice()

# -------------------- Logging Setup --------------------
logging.basicConfig(
    filename="assistant_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_command(command):
    logging.info(f"User Command: {command}")

# -------------------- Greeting --------------------
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sumer")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sumer")
    else:
        speak("Good Evening Sumer")

    speak("How can I help you?")

# -------------------- Command Handler --------------------
def handle_query(query):
    query = query.lower().strip()
    log_command(query)

    websites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "stackoverflow": "https://stackoverflow.com",
        "linkedin": "https://www.linkedin.com/",
        "hacker rank": "https://www.hackerrank.com/",
        "kaggle": "https://www.kaggle.com/",
        "chatgpt": "https://chat.openai.com/",
        "guvi": "https://www.guvi.in/",
        "whatsapp": "https://web.whatsapp.com/",
        "mail": "https://mail.google.com/",
        "instagram": "https://www.instagram.com/",
        "spotify": "https://open.spotify.com/"
    }

    try:
        # 🌐 Website Opening
        for key in websites:
            if key in query:
                speak(f"Opening {key}")
                webbrowser.open(websites[key])
                return

        # 🔎 Google Search
        if "search" in query:
            search_query = query.replace("search", "")
            url = f"https://www.google.com/search?q={search_query}"
            speak(f"Searching for {search_query}")
            webbrowser.open(url)
            return

        # 🎵 Random Song Play
        if "play music" in query:
            music_dir = r'D:\Non Critical\songs\Favorite Songs2'
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    song = random.choice(songs)
                    speak("Playing your favorite song")
                    os.startfile(os.path.join(music_dir, song))
                else:
                    speak("No songs found")
            else:
                speak("Music folder not found")
            return

        # 🎧 Spotify Song Search
        if "play on spotify" in query:
            song_name = query.replace("play on spotify", "")
            speak(f"Playing {song_name} on Spotify")
            webbrowser.open(f"https://open.spotify.com/search/{song_name}")
            return

        # 🕒 Time
        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            return

        # 📅 Date
        if "date" in query:
            today = datetime.date.today()
            speak(f"Today's date is {today}")
            return

        # 💻 Open VS Code
        if "open code" in query:
            codePath = r"C:\Users\Haris\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            if os.path.exists(codePath):
                speak("Opening Visual Studio Code")
                os.startfile(codePath)
            else:
                speak("VS Code path not found")
            return

        # 🔁 Restart
        if "restart system" in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 5")
            return

        # ⛔ Shutdown
        if "shutdown system" in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 5")
            return

        speak("Sorry, I did not understand the command.")

    except Exception as e:
        speak("Something went wrong")
        logging.error(f"Error: {str(e)}")

# -------------------- Run Loop --------------------
if __name__ == "__main__":
    greet()
    while True:
        query = input("Enter Command: ")
        if query.lower() == "exit":
            speak("Goodbye Sumer")
            sys.exit()
        handle_query(query)
