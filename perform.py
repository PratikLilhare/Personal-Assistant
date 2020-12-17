import pyttsx3
import datetime
import speech_recognition as sr

import webbrowser
import os
import smtplib
import play_song
import voice_check
import Speak
import search_wiki





def perform(query):
    
    try:
        query = query.lower()
        # Logic for executing tasks based on query

        if 'youtube' in query:
            Speak.say("opening youtube")
            webbrowser.open("www.youtube.com")

        elif 'google' in query:
            Speak.say("opening google")
            webbrowser.open("www.google.com/hey")

        elif 'open stackoverflow' in query:
            Speak.say("opening stackoverflow")
            webbrowser.open("www.stackoverflow.com")   


        elif 'song' in query or 'play' in query:
            Speak.say('wait a second ')
            #print(query)
            play_song.main(query)

            
        elif 'restart' in query:
            os.system("shutdown /r /t 1");

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            Speak.say(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C://Users//Dell//AppData//Local//Programs//Python//Python36//python.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                Speak.say('opening gmail...')
                url = "https://mail.google.com/mail/"
                webbrowser.open_new(url)
                
            except Exception as e:
                print(e)
                Speak.say("Sorry  I am not able to open mail") 

        else:
            res=search_wiki.search(query)
            print(res)
            return res

    except Exception as e: 
        #ChatLog.insert(END, "Bot: " + "cannot connect at the moment" + '\n\n')
        return "processing....."
