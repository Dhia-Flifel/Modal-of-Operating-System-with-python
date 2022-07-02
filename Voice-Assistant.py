from re import search
import speech_recognition as sr
import webbrowser
import time
import os
import playsound
from gtts import gTTS



print("""
██╗░░░██╗░█████╗░██╗░█████╗░███████╗
██║░░░██║██╔══██╗██║██╔══██╗██╔════╝
╚██╗░██╔╝██║░░██║██║██║░░╚═╝█████╗░░
░╚████╔╝░██║░░██║██║██║░░██╗██╔══╝░░
░░╚██╔╝░░╚█████╔╝██║╚█████╔╝███████╗
░░░╚═╝░░░░╚════╝░╚═╝░╚════╝░╚══════╝

░█████╗░░██████╗░██████╗██╗░██████╗████████╗░█████╗░███╗░░██╗████████╗
██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗░██║╚══██╔══╝
███████║╚█████╗░╚█████╗░██║╚█████╗░░░░██║░░░███████║██╔██╗██║░░░██║░░░
██╔══██║░╚═══██╗░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══██║██║╚████║░░░██║░░░
██║░░██║██████╔╝██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░╚███║░░░██║░░░
╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░""")
#Step1 
r = sr.Recognizer()
def record():
    
    with sr.Microphone() as source:
        print('how can I help you ?')
        audio = r.listen(source)
        voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
        
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
        
    except sr.RequestError:
        print("Sorry, my speech service is down")
        
    return voice_data

def respond(voice_data):
    if 'your name' in voice_data:
        print("my name is sofia.")
    if "how old are you" in voice_data:
        print("I never give my age.")
    if "hey come on" in voice_data:
        print("are you joking with me or what?")
    if "what time is it" in voice_data:
        print("the time is" + time.ctime)
    if "find location" in voice_data:
        "the time is"
    if "search" in voice_data:
        search = record("what do you want to search for?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print("this is what I found for you." + search)
    if "find location" in voice_data:
        location = record("what is the location?")
        url = 'https://www.google.tn/maps/place' + location + '&amp;'
        webbrowser.get().open(url)
        print("here is the location of" + location)              
        
    if 'exit' in voice_data:
        exit()
            
    

voice_data = record()    
print(voice_data) 
respond(voice_data)      
            
    