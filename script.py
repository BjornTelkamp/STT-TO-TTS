import speech_recognition as sr
import pyttsx3
import sys

def transcribe_speech(language='en-US'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language=language)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def speak_text(text, language='en'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for voice in voices:
        if language in voice.languages:
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        language = sys.argv[1]
    else:
        language = 'en-US'

    print(language)
    while True:
        text = transcribe_speech(language=language)
        if text:
            speak_text(text, language=language)
