import speech_recognition as sr     # importing sepech recognizition package as sr
from time import ctime      
import webbrowser
import time
import os
import playsound
import random
from gtts import gTTS
r=sr.Recognizer()        # to recognize speech
def record_voice(ask=False):                      # here we took an optional variable ask which is optional that's why is put to False
    with sr.Microphone() as source:                 # as we ae using mirophones as our source
        if ask:
            #print(ask)
            assistant_speaks(ask)         # calling assistant_speaks function
        audio=r.listen(source)                     # we call listen method to listen our data sent by mic
        voice_data=''                                            # here we took an empty string variable
        try:                               # using try block as an exception handler
            voice_data=r.recognize_google(audio)            # here we put our voice inside our empty string variable
        except sr.UnknownValueError:                      # using except to handle exception when our assistant is unable to recognize voice ex-noise as an input
            #print("Sorry, I didn't get it")
            assistant_speaks("Sorry, I didn't get it")
        except sr.RequestError:
            #print("Sorry, my speech service is down")
            assistant_speaks("Sorry, my speech service is down")
        return voice_data


def assistant_speaks(audio_string):      # function for text to speech conversion where we pass use audio as input
    text_to_speech=gTTS(text=audio_string,lang='en')    # variable storing user audio
    r=random.randint(1,100000)
    audio_file='audio-'+str(r)+ '.mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):      # function to respond to user voice(input)
    if 'what is your name' in voice_data:          # if the voice ask for your name
        #print("My name is Akash Assistant")               # assisant will give this message
        assistant_speaks("My name is Akash Assistant")

    if 'how are you' in voice_data:           # if the voice ask about how are you
        #print("I'm fine. What about you?")    # assiatant will give this message
        assistant_speaks("I'm fine. What about you?")

    if "I am fine" in voice_data:           # if the user says that he is fine
        #print("Nice to know")           # assistant will give this message
        assistant_speaks("Ohh nice to know")

    if 'what time is it'in voice_data:             # if the user ask for current time
        #print(ctime())            # my assistant will show him/her current date and time
        assistant_speaks(ctime())

    if 'search' in voice_data:         # if user want to search something he/she have to say search
        search=record_voice('What do you want to search for?')      # then this message will be shown to user
        url='http://google.com/search?q='+search     # url created for searching in google
        webbrowser.get().open(url)        # here our browser will be opened with results
        #print("Here is what I found for "+ search)
        assistant_speaks("Here is what I found for "+ search)

    if 'find location' in voice_data:         # if user want to find any location
        location=record_voice('What is the location')      # then this message will be shown to user
        url='http://google.nl/maps/place/'+location + '/&amp;'    # url created for searching location in google maps
        webbrowser.get().open(url)        # here our browser will be opened with results
        #print("Here is the location "+ location)
        assistant_speaks("Here is the location "+ location)

    if 'exit' in voice_data:       # to exit our program if voice data is exit
        assistant_speaks("Thanks for using me. I hope you liked me.")
        exit()

time.sleep(1)
#print("How can I help you?: ")      # message from our assistant to the user
assistant_speaks("How can I help you?:" )
while(1):
    voice_data=record_voice()             # storing value returned by function
    respond(voice_data)
