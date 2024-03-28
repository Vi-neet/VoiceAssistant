import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.name == 'espeak-ng-usb-en-1-m5':
            engine.setProperty('voice', voice.id)
    engine.setProperty('rate', 174)
    # eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        # time.sleep(2)
        eel.ShowHood()
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands():
    query=takecommand()
    print(query)

    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    else:
        print("not run")
        
  