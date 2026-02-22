import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import datetime
import wikipedia
import webbrowser
import threading

class SimpleJarvis:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS 2.0 - Simple Version")
        self.root.geometry("700x550")
        self.root.configure(bg='#0a0e27')
        
        # Initialize text-to-speech
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 180)
        
        self.create_ui()
        self.root.after(500, self.welcome)
    
    def create_ui(self):
        # Header
        header = tk.Label(self.root, text="🤖 JARVIS 2.0", 
                         font=('Arial', 24, 'bold'),
                         fg='#00d9ff', bg='#0a0e27')
        header.pack(pady=20)
        
        # Chat Display
        self.chat_display = scrolledtext.ScrolledText(self.root,
                                                       wrap=tk.WORD,
                                                       width=70,
                                                       height=18,
                                                       font=('Consolas', 10),
                                                       bg='#1a1f3a',
                                                       fg='#ffffff',
                                                       relief='flat',
                                                       padx=10,
                                                       pady=10)
        self.chat_display.pack(padx=20, pady=10)
        self.chat_display.config(state='disabled')
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg='#0a0e27')
        input_frame.pack(padx=20, pady=10, fill='x')
        
        self.command_entry = tk.Entry(input_frame,
                                      font=('Arial', 12),
                                      bg='#1a1f3a',
                                      fg='#ffffff',
                                      insertbackground='#00d9ff',
                                      relief='flat')
        self.command_entry.pack(side='left', fill='x', expand=True, ipady=8)
        self.command_entry.bind('<Return>', lambda e: self.process_input())
        
        send_btn = tk.Button(input_frame, text="▶ Send",
                           command=self.process_input,
                           font=('Arial', 11, 'bold'),
                           bg='#00d9ff',
                           fg='#0a0e27',
                           width=10,
                           relief='flat',
                           cursor='hand2')
        send_btn.pack(side='right', padx=(10, 0))
        
        # Quick Buttons
        quick_frame = tk.Frame(self.root, bg='#0a0e27')
        quick_frame.pack(pady=5)
        
        buttons = [
            ("Google", "google"),
            ("YouTube", "youtube"),
            ("Time", "time"),
            ("Help", "help")
        ]
        
        for text, cmd in buttons:
            btn = tk.Button(quick_frame, text=text,
                          command=lambda c=cmd: self.quick_command(c),
                          font=('Arial', 9),
                          bg='#1a1f3a',
                          fg='#ffffff',
                          width=12,
                          relief='flat',
                          cursor='hand2')
            btn.pack(side='left', padx=5)
    
    def add_message(self, sender, message, color='#ffffff'):
        self.chat_display.config(state='normal')
        time = datetime.datetime.now().strftime("%H:%M")
        self.chat_display.insert(tk.END, f"\n[{time}] {sender}:\n", 'sender')
        self.chat_display.insert(tk.END, f"{message}\n", 'msg')
        self.chat_display.tag_config('sender', foreground='#00d9ff', font=('Consolas', 10, 'bold'))
        self.chat_display.tag_config('msg', foreground=color)
        self.chat_display.see(tk.END)
        self.chat_display.config(state='disabled')
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def welcome(self):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            greeting = "Good Morning!"
        elif 12 <= hour < 18:
            greeting = "Good Afternoon!"
        else:
            greeting = "Good Evening!"
        
        msg = f"{greeting} I'm JARVIS. Type a command or use quick buttons!"
        self.add_message("JARVIS", msg, '#00ff00')
        threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
    
    def process_input(self):
        query = self.command_entry.get().strip().lower()
        if not query:
            return
        
        self.add_message("You", query, '#00d9ff')
        self.command_entry.delete(0, tk.END)
        self.process_command(query)
    
    def quick_command(self, cmd):
        self.command_entry.delete(0, tk.END)
        self.command_entry.insert(0, cmd)
        self.process_input()
    
    def process_command(self, query):
        try:
            # Wikipedia
            if 'wikipedia' in query:
                response = "Searching Wikipedia..."
                self.add_message("JARVIS", response, '#ffff00')
                query_clean = query.replace("wikipedia", "").strip()
                try:
                    result = wikipedia.summary(query_clean, sentences=2)
                    self.add_message("JARVIS", f"Wikipedia: {result}", '#00ff00')
                    threading.Thread(target=self.speak, args=(result,), daemon=True).start()
                except:
                    err = "Sorry, couldn't find that on Wikipedia."
                    self.add_message("JARVIS", err, '#ff0000')
                    threading.Thread(target=self.speak, args=(err,), daemon=True).start()
            
            # Websites
            elif 'youtube' in query or query == 'youtube':
                msg = "Opening YouTube"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
                webbrowser.open("https://youtube.com")
            
            elif 'google' in query or query == 'google':
                msg = "Opening Google"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
                webbrowser.open("https://google.com")
            
            elif 'chatgpt' in query:
                msg = "Opening ChatGPT"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
                webbrowser.open("https://chat.openai.com")
            
            elif 'linkedin' in query:
                msg = "Opening LinkedIn"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
                webbrowser.open("https://linkedin.com")
            
            elif 'instagram' in query:
                msg = "Opening Instagram"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
                webbrowser.open("https://instagram.com")
            
            elif 'whatsapp' in query:
                msg = "Opening WhatsApp"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
                webbrowser.open("https://web.whatsapp.com")
            
            elif 'gmail' in query or 'mail' in query:
                msg = "Opening Gmail"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
                webbrowser.open("https://mail.google.com")
            
            elif 'stackoverflow' in query:
                msg = "Opening Stack Overflow"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
                webbrowser.open("https://stackoverflow.com")
            
            # Time & Date
            elif 'time' in query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                msg = f"The time is {time}"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
            
            elif 'date' in query:
                date = datetime.datetime.now().strftime("%B %d, %Y")
                msg = f"Today is {date}"
                self.add_message("JARVIS", msg)
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
            
            # Help
            elif 'help' in query:
                help_text = """Commands you can use:
• wikipedia [topic] - Search Wikipedia
• google - Open Google
• youtube - Open YouTube
• chatgpt - Open ChatGPT
• time - Get current time
• date - Get current date
• linkedin - Open LinkedIn
• instagram - Open Instagram
• gmail - Open Gmail
• exit - Close assistant"""
                self.add_message("JARVIS", help_text, '#ffff00')
            
            # Exit
            elif 'exit' in query or 'quit' in query or 'bye' in query:
                msg = "Goodbye! Have a great day!"
                self.add_message("JARVIS", msg, '#ff9900')
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
                self.root.after(2000, self.root.destroy)
            
            else:
                msg = "I didn't understand. Type 'help' to see available commands."
                self.add_message("JARVIS", msg, '#ff9900')
                threading.Thread(target=self.speak, args=(msg,), daemon=True).start()
        
        except Exception as e:
            err = f"Error: {str(e)}"
            self.add_message("System", err, '#ff0000')

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleJarvis(root)
    root.mainloop()
