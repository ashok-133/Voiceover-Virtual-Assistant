#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:00:09 2020

@author: kandagadlaashokkumar
"""
from gtts import gTTS
import playsound
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("YOUR EMAIL","YOUR PASSWORD")
    server.sendmail("YOUR EMAIL", to, content)

def speak(mytext):
    tts = gTTS(text = mytext, lang = 'en',slow =False)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
    
def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning ashok!")
        speak("Good morning ashok!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        speak("Good eveing!")
        speak("Good evening!")
    print("I am Jarvis sir, Here to help you!!!")
    speak("I am Jarvis sir, Here to help you")

    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"user said:{query}\n")
    except:
        print("Say that again please...")
        return "None"
    return query

Wishme()
while True:
    query = takecommand().lower()
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        speak("Opening youtube")
        webbrowser.open('https://youtube.com', new=2)
    elif 'geetam' in query:
        speak("opening Gitam website")
        webbrowser.open("https://gitam.edu",new=2)
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is  {strTime}")
        print(f"The time is  {strTime}")
    elif 'coursera' in query:
        speak("opening coursera website")
        webbrowser.open("https://coursera.org",new=2)
    elif 'send email to ashok' in query:
        try:
            print("what should i have to send sir?")
            speak("what should i have to send sir?")
            content = takecommand()
            to = "RECEIVER EMAIL"
            sendEmail(to,content)
            print("Email has been sent sir")
            speak("Email has been sent sir")
            
        except:
            speak("Not able to here sir")
    elif 'corona' in query:
        speak("Loading sir")
        webbrowser.open("https://www.mohfw.gov.in/",new=2)
    
    elif 'goodbye' in query:
        print("until next time")
        speak("until next time")
        break
        
        
        

        
    
     



