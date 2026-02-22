import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import openai
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello sir, I am prasad. How can I assist you?")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'linkdin' in query:
            webbrowser.open("https://www.linkedin.com/in/sumersing-patil-839674234/")   
        elif 'hacker rank' in query:
            webbrowser.open("https://www.hackerrank.com/sumerrajput0193?hr_r=1")   
        elif 'kaggle' in query:
            webbrowser.open("https://www.kaggle.com/sumersingpatil2694")  
        elif 'play musi' in query:
            webbrowser.open("https://www.youtube.com/watch?v=xvIfmuJpF14&list=WL&index=2")    
        elif 'chatgpt' in query:
            webbrowser.open("https://chat.openai.com/") 
        elif 'open chatgpt' in query:
            webbrowser.open("https://chat.openai.com/")     
        elif 'hacker rank' in query:
            webbrowser.open("https://www.hackerrank.com/sumerrajput0193?hr_r=1")     
        elif 'guvi' in query:
            webbrowser.open("https://www.guvi.in/courses.html?current_tab=myCourses")
        elif 'Whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open google photos videos' in query:
            webbrowser.open("https://photos.google.com/?pli=1")    
        elif 'Mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
        elif 'Instagram' in query:
            webbrowser.open("https://www.instagram.com/_sumerrajput2694_/")
        elif 'open sagar patil ' in query:
            webbrowser.open("https://www.instagram.com/patilsagarashok/")
        