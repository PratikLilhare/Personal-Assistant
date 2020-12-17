import pyttsx3
import datetime
import speech_recognition as sr

import Speak


def takeCommand():
    # it takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        print("Listening.....")
        Speak.say('Listening.....')
        r.pause_threshold = 0.7
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        #print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        #print("Say that again please....")
        Speak.say("Say that again please....")

        return "None"
    
    return query
