import tkinter as tk
from tkinter import ttk, scrolledtext
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import threading
from PIL import Image, ImageTk
import requests
from io import BytesIO

class JarvisAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS 2.0 - AI Voice Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg='#0a0e27')
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 180)
        
        self.is_listening = False
        
        # Create UI
        self.create_ui()
        
        # Welcome message
        self.root.after(500, self.wish_me)
    
    def create_ui(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg='#1a1f3a', height=80)
        header_frame.pack(fill='x', pady=(0, 10))
        header_frame.pack_propagate(False)
        
        # Title
        title = tk.Label(header_frame, text="🤖 JARVIS 2.0", 
                        font=('Arial', 28, 'bold'),
                        fg='#00d9ff', bg='#1a1f3a')
        title.pack(pady=15)
        
        # Status Frame
        status_frame = tk.Frame(self.root, bg='#0a0e27')
        status_frame.pack(pady=10)
        
        self.status_label = tk.Label(status_frame, text="● Ready", 
                                     font=('Arial', 12),
                                     fg='#00ff00', bg='#0a0e27')
        self.status_label.pack()
        
        # Chat Display Area
        chat_frame = tk.Frame(self.root, bg='#0a0e27')
        chat_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        self.chat_display = scrolledtext.ScrolledText(chat_frame,
                                                       wrap=tk.WORD,
                                                       width=70,
                                                       height=15,
                                                       font=('Consolas', 11),
                                                       bg='#1a1f3a',
                                                       fg='#ffffff',
                                                       insertbackground='#00d9ff',
                                                       relief='flat',
                                                       padx=10,
                                                       pady=10)
        self.chat_display.pack(fill='both', expand=True)
        self.chat_display.config(state='disabled')
        
        # Control Buttons Frame
        control_frame = tk.Frame(self.root, bg='#0a0e27')
        control_frame.pack(pady=20)
        
        # Voice Button
        self.voice_btn = tk.Button(control_frame, text="🎤 Voice Command",
                                   command=self.start_listening,
                                   font=('Arial', 14, 'bold'),
                                   bg='#00d9ff',
                                   fg='#0a0e27',
                                   width=18,
                                   height=2,
                                   relief='flat',
                                   cursor='hand2',
                                   activebackground='#00b3cc')
        self.voice_btn.grid(row=0, column=0, padx=10)
        
        # Text Input Button
        self.text_btn = tk.Button(control_frame, text="⌨️ Type Command",
                                  command=self.text_command,
                                  font=('Arial', 14, 'bold'),
                                  bg='#7c3aed',
                                  fg='#ffffff',
                                  width=18,
                                  height=2,
                                  relief='flat',
                                  cursor='hand2',
                                  activebackground='#6d28d9')
        self.text_btn.grid(row=0, column=1, padx=10)
        
        # Quick Actions Frame
        quick_frame = tk.LabelFrame(self.root, text="Quick Actions",
                                   bg='#0a0e27', fg='#00d9ff',
                                   font=('Arial', 11, 'bold'),
                                   relief='flat')
        quick_frame.pack(pady=10, padx=20, fill='x')
        
        quick_buttons = [
            ("🌐 Google", lambda: self.quick_open("google")),
            ("▶️ YouTube", lambda: self.quick_open("youtube")),
            ("💬 ChatGPT", lambda: self.quick_open("chatgpt")),
            ("🕐 Time", lambda: self.quick_action("time")),
        ]
        
        for i, (text, command) in enumerate(quick_buttons):
            btn = tk.Button(quick_frame, text=text,
                          command=command,
                          font=('Arial', 10),
                          bg='#1a1f3a',
                          fg='#ffffff',
                          width=15,
                          relief='flat',
                          cursor='hand2',
                          activebackground='#2a2f4a')
            btn.grid(row=0, column=i, padx=5, pady=10)
    
    def add_message(self, sender, message, color='#ffffff'):
        self.chat_display.config(state='normal')
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"\n[{timestamp}] {sender}:\n", 'sender')
        self.chat_display.insert(tk.END, f"{message}\n", 'message')
        self.chat_display.tag_config('sender', foreground='#00d9ff', font=('Consolas', 11, 'bold'))
        self.chat_display.tag_config('message', foreground=color)
        self.chat_display.see(tk.END)
        self.chat_display.config(state='disabled')
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def update_status(self, text, color='#00ff00'):
        self.status_label.config(text=f"● {text}", fg=color)
    
    def wish_me(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            greeting = "Good Morning!"
        elif 12 <= hour < 18:
            greeting = "Good Afternoon!"
        else:
            greeting = "Good Evening!"
        
        message = f"{greeting} I am JARVIS, your AI assistant. How can I help you?"
        self.add_message("JARVIS", message, '#00ff00')
        threading.Thread(target=self.speak, args=(message,), daemon=True).start()
    
    def take_command(self):
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                self.update_status("Listening...", '#ffff00')
                self.add_message("System", "Listening for your command...", '#ffff00')
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
            self.update_status("Recognizing...", '#ff9900')
            self.add_message("System", "Recognizing...", '#ff9900')
            query = r.recognize_google(audio, language='en-in')
            self.add_message("You", query, '#00d9ff')
            return query.lower()
        
        except sr.WaitTimeoutError:
            self.update_status("Ready", '#00ff00')
            self.add_message("System", "No speech detected. Please try again.", '#ff0000')
            return "none"
        except Exception as e:
            self.update_status("Ready", '#00ff00')
            self.add_message("System", "Could not understand. Please try again.", '#ff0000')
            return "none"
    
    def start_listening(self):
        if not self.is_listening:
            self.is_listening = True
            self.voice_btn.config(state='disabled', bg='#888888')
            threading.Thread(target=self.process_voice_command, daemon=True).start()
    
    def process_voice_command(self):
        query = self.take_command()
        if query != "none":
            self.process_command(query)
        
        self.is_listening = False
        self.voice_btn.config(state='normal', bg='#00d9ff')
        self.update_status("Ready", '#00ff00')
    
    def text_command(self):
        # Create input dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Type Command")
        dialog.geometry("400x150")
        dialog.configure(bg='#1a1f3a')
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(dialog, text="Enter your command:",
                font=('Arial', 12),
                bg='#1a1f3a', fg='#ffffff').pack(pady=10)
        
        entry = tk.Entry(dialog, font=('Arial', 12),
                        width=40, bg='#0a0e27',
                        fg='#ffffff', insertbackground='#00d9ff')
        entry.pack(pady=10)
        entry.focus()
        
        def submit():
            query = entry.get().lower()
            if query:
                self.add_message("You", query, '#00d9ff')
                self.process_command(query)
            dialog.destroy()
        
        tk.Button(dialog, text="Submit",
                 command=submit,
                 font=('Arial', 11, 'bold'),
                 bg='#00d9ff', fg='#0a0e27',
                 width=15, cursor='hand2').pack(pady=10)
        
        entry.bind('<Return>', lambda e: submit())
    
    def process_command(self, query):
        try:
            # Wikipedia
            if 'wikipedia' in query:
                self.update_status("Searching Wikipedia...", '#ffff00')
                response = "Searching Wikipedia..."
                self.add_message("JARVIS", response, '#ffff00')
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    response = f"According to Wikipedia: {results}"
                    self.add_message("JARVIS", response, '#00ff00')
                    threading.Thread(target=self.speak, args=(results,), daemon=True).start()
                except:
                    response = "Sorry, I couldn't find that on Wikipedia."
                    self.add_message("JARVIS", response, '#ff0000')
                    threading.Thread(target=self.speak, args=(response,), daemon=True).start()
            
            # Open websites
            elif 'youtube' in query or 'open youtube' in query:
                response = "Opening YouTube"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                webbrowser.open("https://youtube.com")
            
            elif 'google' in query or 'open google' in query:
                response = "Opening Google"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                webbrowser.open("https://google.com")
            
            elif 'stackoverflow' in query:
                response = "Opening Stack Overflow"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                webbrowser.open("https://stackoverflow.com")
            
            elif 'chatgpt' in query or 'open chatgpt' in query:
                response = "Opening ChatGPT"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                webbrowser.open("https://chat.openai.com/")
            
            elif 'linkedin' in query:
                response = "Opening LinkedIn"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                webbrowser.open("https://www.linkedin.com")
            
            elif 'instagram' in query:
                response = "Opening Instagram"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                webbrowser.open("https://www.instagram.com")
            
            elif 'whatsapp' in query:
                response = "Opening WhatsApp Web"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                webbrowser.open("https://web.whatsapp.com/")
            
            elif 'gmail' in query or 'mail' in query:
                response = "Opening Gmail"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                webbrowser.open("https://mail.google.com")
            
            # Time
            elif 'time' in query:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                response = f"Sir, the time is {str_time}"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
            
            # Date
            elif 'date' in query:
                date = datetime.datetime.now().strftime("%B %d, %Y")
                response = f"Today's date is {date}"
                self.add_message("JARVIS", response)
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
            
            # Exit
            elif 'exit' in query or 'quit' in query or 'bye' in query:
                response = "Goodbye sir! Have a great day!"
                self.add_message("JARVIS", response, '#ff9900')
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
                self.root.after(2000, self.root.destroy)
            
            else:
                response = "I'm not sure how to help with that. Try commands like: Wikipedia, YouTube, Google, Time, Date, or Exit."
                self.add_message("JARVIS", response, '#ff9900')
                threading.Thread(target=self.speak, args=(response,), daemon=True).start()
            
            self.update_status("Ready", '#00ff00')
        
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            self.add_message("System", error_msg, '#ff0000')
            self.update_status("Ready", '#00ff00')
    
    def quick_open(self, site):
        sites = {
            "google": "https://google.com",
            "youtube": "https://youtube.com",
            "chatgpt": "https://chat.openai.com/"
        }
        response = f"Opening {site.title()}"
        self.add_message("JARVIS", response)
        threading.Thread(target=self.speak, args=(response,), daemon=True).start()
        webbrowser.open(sites.get(site, "https://google.com"))
    
    def quick_action(self, action):
        if action == "time":
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            response = f"The time is {str_time}"
            self.add_message("JARVIS", response)
            threading.Thread(target=self.speak, args=(response,), daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisAssistant(root)
    root.mainloop()
