from tkinter import *
import itertools
import datetime
import voice_check
import Speak
import perform


def chatbot_response(msg):
    msg=msg.lower()
    if msg == "hi":
        Speak.say("hello how are you")
        return "hello how are you"
    elif msg=='good morning' or msg=='good afternoon' or msg=='good night':
        
        return time_wish()
    elif msg=='bye' or msg=='close' or msg=='exit':
        return bye_wish()
    else:
        Speak.say("processing")
        response=perform.perform(msg)
        if msg!='None':
            return response
        else:
            Speak.say('I am unable to understand')
            return 'I am unable to understand'

    

def voice_command():
    speakbutton['bg'] ='red'
    msg=voice_check.takeCommand()
    speakbutton['bg'] = 'green'
    if msg!='None':
        ChatLog.config(state=NORMAL)
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        res=chatbot_response(msg)
        print(res)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        return res
        

    return msg

def time_wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak.say("Good Morning!")
        return('Good Morning')
        

    elif hour >= 12 and hour < 18:
        Speak.say("Good Afternoon")
        return('Good Afternoon')
       

    else:
        Speak.say("Good Evening")
        return('Good Evening')

def bye_wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 18:
        Speak.say("Have a nice Day!")
    else:
        Speak.say("Good night ...Take Care")
    
    base.destroy()
        
def initiate():
    time_wish()
    Speak.say("How may i help you")
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END,"BOT : How may i help you\n\n")
    ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)
  

def send(event):
    #print("sent")
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 15 ))
            res = chatbot_response(msg)
            #print(res)
            ChatLog.insert(END, "Bot: " + res + '\n\n')
            #perform(msg)
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

def toggle():
    #global icycle
    # works with Python27 and Python3
    state = str(next(icycle))
    if state=='True':
        pass
        
        
    else:
        speakbutton['text'] =''
        speakbutton['bg'] = 'green'
        
    


base = Tk()
base.iconbitmap(r'F:\Downloads\Jarvis\jarvis_icon.ico')
base.title("Assistant")
base.geometry("430x450")
base.configure(background='black')
base.resizable(width=FALSE, height=FALSE)
ChatLog = Text(base, bd=7, bg="white", height="8", width="50", font="Verdana")
ChatLog.config(state=DISABLED)
scrollbar = Scrollbar(base, command=ChatLog.yview,bd=7)
ChatLog['yscrollcommand'] = scrollbar.set

icycle = itertools.cycle([True, False])
SendButton = Button(base, font=("system",13,'bold'), text="Send",
                    bd=5, bg="blue", activebackground="#3c9d9b",fg='#ffffff',
                   )


mic_pic = PhotoImage(file = r"F:\Downloads\Jarvis\mic_pic.png")
Mic = mic_pic.subsample(7,6)


speakbutton = Button(base,image=Mic,
                    compound=LEFT,
                    bd=4, bg="green", activebackground="red",fg='#ffcccc',
                    command=voice_command
                    )
quitbutton = Button(base, font=("System",16,'bold'), text="Close",command=bye_wish,
                    bd=5, bg="red", activebackground="#3c9d9b",fg='#ffffff',
                    )


EntryBox = Text(base, bd=5, bg='white',width="29", height="5", font=("Hermann",14))
scrollbar.place(x=408,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=400)
EntryBox.grid(row=1,column=1,padx=10,pady=10)
SendButton.grid(row=1,column=0,padx=10,pady=10)
speakbutton.grid(row=1,column=3,padx=10,pady=10)
quitbutton.grid(row=1,column=5,padx=10,pady=10)
speakbutton.place(x=295,y=400, height = 45)
EntryBox.place(x=80, y=400, height=43, width=210)
SendButton.place(x=10, y=400, height=45)
quitbutton.place(x=360,y=400,height=45)

#to send command by click 
SendButton.bind('<Button>',send)
#to send command by enter key
EntryBox.bind('<Return>',send)
initiate()
base.mainloop()
