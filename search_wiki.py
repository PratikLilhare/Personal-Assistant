import wikipedia
import Speak
def search(msg):
    Speak.say('Searching Wikipedia about'+msg)
    result=wikipedia.summary(msg,sentences=2)
    #print(result)
    Speak.say(result)
    return result
