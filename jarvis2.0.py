import os
import webbrowser
import datetime
import random
import logging
import pyttsx3

# -------------------- Voice Engine Setup --------------------
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# -------------------- Logging Setup --------------------
logging.basicConfig(
    filename="assistant_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_command(command):
    logging.info(f"User Command: {command}")

# -------------------- Command Handler --------------------
def handle_query(query):
    query = query.lower()
    log_command(query)

    websites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "stackoverflow": "https://stackoverflow.com",
        "linkedin": "https://www.linkedin.com/in/sumersing-patil-839674234/",
        "hacker rank": "https://www.hackerrank.com/sumerrajput0193?hr_r=1",
        "kaggle": "https://www.kaggle.com/sumersingpatil2694",
        "chatgpt": "https://chat.openai.com/",
        "guvi": "https://www.guvi.in/courses.html?current_tab=myCourses",
        "whatsapp": "https://web.whatsapp.com/",
        "mail": "https://mail.google.com/",
        "instagram": "https://www.instagram.com/_sumerrajput2694_/",
        "spotify": "https://open.spotify.com/"
    }

    try:
        # 🌐 Website Opening
        for key in websites:
            if key in query:
                speak(f"Opening {key}")
                webbrowser.open(websites[key])
                return

        # 🎵 Random Song Play
        if "play music" in query:
            music_dir = r'D:\Non Critical\songs\Favorite Songs2'
            songs = os.listdir(music_dir)

            if songs:
                song = random.choice(songs)
                speak("Playing your music")
                os.startfile(os.path.join(music_dir, song))
            else:
                speak("No songs found")
            return

        # 🕒 Time
        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            return

        # 💻 Open VS Code
        if "open code" in query:
            codePath = r"C:\Users\Haris\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            speak("Opening Visual Studio Code")
            os.startfile(codePath)
            return

        speak("Sorry, I did not understand the command.")

    except Exception as e:
        speak("Something went wrong")
        logging.error(f"Error: {str(e)}")

# -------------------- Run Loop --------------------
if __name__ == "__main__":
    while True:
        query = input("Enter Command: ")
        if query == "exit":
            speak("Goodbye")
            break
        handle_query(query)
