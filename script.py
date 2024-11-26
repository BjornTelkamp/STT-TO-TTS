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
