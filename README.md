# JARVIS 2.0 - AI Voice Assistant
# Modern UI Version for Freshers

## Features:
- 🎤 Voice Command Recognition
- ⌨️ Text Command Input
- 🌐 Quick Website Access (Google, YouTube, ChatGPT, etc.)
- 🕐 Time & Date Functions
- 📚 Wikipedia Search
- 🎨 Modern Dark Theme UI
- 💬 Chat-style Display

## Installation:

### Step 1: Install Required Libraries
```bash
pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia
pip install pyaudio
pip install pillow
```

### Step 2: For Microphone Access (PyAudio)
**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Linux/Mac:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

## How to Run:
```bash
python jarvis_ui.py
```

## Voice Commands:
- "Wikipedia [topic]" - Search Wikipedia
- "Open YouTube" - Opens YouTube
- "Open Google" - Opens Google
- "Open ChatGPT" - Opens ChatGPT
- "What's the time" - Tells current time
- "What's the date" - Tells current date
- "Open LinkedIn" - Opens LinkedIn
- "Open Instagram" - Opens Instagram
- "Open WhatsApp" - Opens WhatsApp Web
- "Open Gmail" - Opens Gmail
- "Exit/Quit/Bye" - Closes the assistant

## UI Features:
1. **Voice Command Button** - Click and speak your command
2. **Type Command Button** - Type your command manually
3. **Quick Actions** - One-click buttons for common tasks
4. **Chat Display** - Shows conversation history
5. **Status Indicator** - Shows current status (Ready/Listening/Processing)

## Tips for Freshers:
- Speak clearly when using voice commands
- Wait for "Listening..." status before speaking
- Use Type Command if voice recognition isn't working
- Try Quick Actions for instant results
- Check the chat display for responses

## Troubleshooting:

### Microphone Not Working:
- Check microphone permissions in system settings
- Try using "Type Command" instead
- Install PyAudio properly using steps above

### Voice Not Working:
- Ensure speakers are on
- pyttsx3 should work offline
- Check system audio settings

### Import Errors:
Make sure all libraries are installed:
```bash
pip install -r requirements.txt
```

## Customization:
- Change voice: Modify `self.engine.setProperty('voice', voices[1].id)` 
  - Use voices[0] for male voice
  - Use voices[1] for female voice
- Change colors: Edit hex color codes in the UI section
- Add more commands: Add elif conditions in `process_command()` method

## Created for Freshers 💡
Simple, working, and professional!
