import random

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audios):
    engine.say(audios)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audios = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audios, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    with open('password.txt') as f: # create a txt file and save your password
        a=f.read()
    server.login('your-email',a) # a = write your password
    server.sendmail('sender-email',to,content) # write sender emil address
    server.close()



if __name__ == "__main__":
    wishMe()
    t=True
    while t:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(f"{results}")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir= 'C:\\Users\\soham\\Music\\musics' #path file of music
            songs=os.listdir(music_dir) # list create hoga music ka
            print(songs)
            value=random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[value]))
        elif 'the time ' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,The time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\soham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # path of visual code
            os.startfile(codePath)

        elif 'email to loknath' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to='sender- email' # write a email address to whom you want to sent the email
                sendEmail(to,content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry sir , I am unbale to send this email")

        elif 'exit' in query:
            t=False
