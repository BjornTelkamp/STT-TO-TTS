# Speech-to-Text and Text-to-Speech

This script uses speech recognition to transcribe spoken words into text and then uses text-to-speech to speak out the
transcribed text. It's useful for applications where you want to convert spoken words into synthesized speech.

## Prerequisites

* Python 3.12 or higher

* speech_recognition library

* pyttsx3 library

* pyaudio library

## Installation

### Step 1: Install Python

If you don't have Python installed, download and install it from
the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Required Libraries

Install speech_recognition:

```sh
pip install SpeechRecognition
```

Install pyttsx3:

```sh
pip install pyttsx3
```

Install pyaudio:

* Windows:

```sh
pip install pyaudio
```

* macOS:

```sh
brew install portaudio
pip install pyaudio
```

* Linux:

```sh
sudo apt-get install python3-pyaudio
```

## Usage

Save the Script: Save the following script as script.py:

```php
import speech_recognition as sr
import pyttsx3

def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def speak_text(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.id == 0:
            engine.setProperty('voice', voice.id)
            break
            
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        text = transcribe_speech()
        if text:
        speak_text(text)
```

Run the Script: Open a terminal or command prompt, navigate to the directory where transcribe.py is saved, and run:

```sh
python script.py
```
