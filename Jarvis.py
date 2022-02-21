import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install SpeechRecognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source,0,5)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User Said: {query}\n')

    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query.lower()

if __name__ == "__main__":
    while True:
        query = listen().lower()
