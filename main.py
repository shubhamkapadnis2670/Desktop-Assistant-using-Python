
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os


#taking voice from my system
engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
#print(voices[1])
engine.setProperty('voice', voices[0].id)

#speak function
def speak(text):
    """This function take text as input and returns audio

    Args:
        text (_type_): _description_
    """
    engine.say(text)
    engine.runAndWait()

speak("I am programmer? what about you? i am shubham dayaram kapadnis.")