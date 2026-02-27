import os
import sys
import webbrowser
import datetime
import logging

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
