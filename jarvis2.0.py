import os
import webbrowser
import datetime
import pyttsx3
import wikipedia
import psutil

# -------------------- Text To Speech --------------------

engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak(text):
    """Speak and print text"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


# -------------------- Greeting --------------------

def greet():
    hour = datetime.datetime.now().hour

    if hour < 12:
        message = "Good Morning Sumer"
    elif hour < 18:
        message = "Good Afternoon Sumer"
    else:
        message = "Good Evening Sumer"

    speak(message)


# -------------------- Time --------------------

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")


# -------------------- Date --------------------

def tell_date():
    today = datetime.date.today().strftime("%d %B %Y")
    speak(f"Today's date is {today}")


# -------------------- Open VS Code --------------------

def open_vscode():
    vscode_paths = [
        r"C:\Users\Haris\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        r"C:\Program Files\Microsoft VS Code\Code.exe"
    ]

    for path in vscode_paths:
        if os.path.exists(path):
            os.startfile(path)
            speak("Opening Visual Studio Code")
            return

    speak("Visual Studio Code not found")


# -------------------- Spotify --------------------

def play_on_spotify(query):
    song = query.replace("play on spotify", "").strip()

    if not song:
        speak("Please tell me the song name")
        return

    url = f"https://open.spotify.com/search/{song}"
    webbrowser.open(url)
    speak(f"Playing {song} on Spotify")


# -------------------- Wikipedia --------------------

def search_wikipedia(query):
    topic = query.replace("wikipedia", "").strip()

    if not topic:
        speak("Please tell me what to search")
        return

    try:
        result = wikipedia.summary(topic, sentences=2)
        speak("According to Wikipedia")
        speak(result)

    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please be more specific.")

    except Exception:
        speak("Sorry I couldn't find information.")


# -------------------- System Info --------------------

def system_info():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    speak(f"CPU usage is {cpu} percent")
    speak(f"Memory usage is {memory} percent")


# -------------------- Command Handler --------------------

def handle_command(query):

    query = query.lower().strip()

    commands = {

        "time": tell_time,
        "date": tell_date,
        "open vscode": open_vscode,
        "system status": system_info
    }

    # direct commands
    for key in commands:
        if key in query:
            commands[key]()
            return

    # spotify
    if "play on spotify" in query:
        play_on_spotify(query)

    # exit
    elif "exit" in query or "quit" in query:
        speak("Goodbye Sumer")
        exit()

    else:
        speak("Sorry I did not understand")


# -------------------- Main --------------------

def main():

    greet()

    while True:
        query = input("Enter command: ")
        handle_command(query)
        import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)

        try:
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

        except:
            command = ""
            print("Sorry, say again")

    return command


def run_jarvis():

    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif "stop" in command:
        speak("Goodbye")
        exit()


while True:
    run_jarvis()


if __name__ == "__main__":
    main()


