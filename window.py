from tkinter import *
from multiprocessing import Process

import AppOpener
from PIL import Image, ImageTk
import speech_recognition as sr
import datetime
import pyaudio
import pyttsx3
import pywhatkit as kt
#from PyDictionary import PyDictionary
from threading import Thread
import pyjokes
import webbrowser
from AppOpener import *
import wolframalpha
from ecapture import ecapture as ec
import os
from math import *


engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 145)

global name
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# create a window and set background colour as black
root = Tk()
root.title('WAGNER')
root.geometry('500x500')
root.configure(bg='black')

menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu, font=("Helvetica", "10"))
file_menu.add_command(label='About WAGNER', font=("Helvetica", "10"))
file_menu.add_command(label='commands', font=("Helvetica", "10"))
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit, font=("Helvetica", "10"))
help_menu = Menu(menu)
menu.add_cascade(label='Help', menu=help_menu, font=("Helvetica", "10"))
help_menu.add_command(label='About', font=("Helvetica", "10"))

frame1 = Frame(root, height=500, width=200, bg='black')
frame1.pack()

count = 0
anim = None

image = Image.open('mic.png')
img = image.resize((50, 50))
photo = ImageTk.PhotoImage(img)
btn = Button(frame1, bg='black', image=photo, command=lambda: animation(count))
btn.pack(pady=10)

label = Label(frame1, bg="black", fg="white", text="Tap the mic to speak", font=("Helvetica", "16"))
label.pack()

file = "wave_sound.gif"
image1 = Image.open(file)
image1.resize((200, 200))
frames = image1.n_frames  # gives the number of frames in the gif
# creating list of PhotoImage objects from the number of frames
im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]
photo1 = ImageTk.PhotoImage(image1)
label1 = Label(frame1, bg="black", image=photo1)
label1.pack()

def having(text,subtext):
    for i in subtext:
        if i in text:
            return True
    return False



def command(query):


    """ Interactions : """
    if having(query,['you know my name','my name']):
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            speak("Sorry human i don't know your name, what would you like me to call you ?")
            print("Listening")
            bot_status(True)
            uservoice = r.listen(mic)
            print("Recognizing")
            bot_status(False, True)
            query = r.recognize_google(uservoice)
            name =query.replace("my name is","")
            speak("Jay Shree Ram Ram "+name+" I am you voice assistance Rudra, nice to meet you")

    if having(query,['task','perform','what can you do']):
        speak("Ruk bataata hu mei kya kar sakta hu..")
        tAsk="C:\\Users\\Ayush Panigrahi\\PycharmProjects\\voice_assistant\\jarvis.txt"
        os.startfile(tAsk)

    if having(query,["who are you","who made you"]):
        Me = "C:\\Users\\Ayush Panigrahi\\PycharmProjects\\voice_assistant\\about.txt"
        os.startfile(Me)
        speak("Hii, I am a voice assistant namely Nigga made by Krithik, Ayush, Unnati")

        bot_status(False,False,True)

    if having(query,["you are good","you are nice","you are awesome"]):
        message(text="Aww thank you, I appreciate that", bot=True)
        speak("Aww thank you, I appreciate that")
        bot_status(False,False,True)

    if having(query,["tell me some jokes","make me laugh"]):
        jokes=pyjokes.get_joke()
        message(text=f"{jokes}", bot=True)
        speak(f"{jokes}")
        bot_status(False,False,True)


    if having(query,["how are you"]):
        message(text="I am good. Thank You. What about You?", bot=True)
        speak("I am good. Thank You. What about you?")
        uservoice1=record()
        if having(uservoice1,["not feeling good","sad","not fine","not good"]):
            message("Dont worry, Everything will be fine soon",True)
            speak("Dont worry, Everything will be fine soon")
        else:
            message("Thats really nice. Have a great day ", True)
            speak("Thats really nice. Have a great day")
        bot_status(False, False, True)

    """ PLAYING VIDEO OR SEARCHING ON YOUTUBE """

    if having(query,["on youtube","video","play"]):
        if "play" in query:
            query=query.replace('play','')
        if "video" in query:
            query=query.replace('video','')
        if "on youtube" in query:
            query=query.replace('on youtube','')
        message(text=f"Opening Youtube and playing {query}", bot=True)
        speak(f"Hold on, Loading Youtube and playing {query}.")
        kt.playonyt(query)
        bot_status(False, False, True)

    """ SEARCHING ON GOOGLE """

    if having(query,["search","google","on google"]):
        if "search" in query:
            query=query.replace('search','')
        if "on google" in query:
            query = query.replace('on google', '')
        if "google" in query:
            query = query.replace('google', '')

        message(text=f"Searching:{query} on Google", bot=True)
        speak(f"Hold on, I am searching {query} on Google.")
        kt.search(query)
        bot_status(False, False, True)

    # Snake game command
    if having(query,['games','open game']):
        message("Let's have some fun with our games.....")
        speak("opening the snake game ")
        import snake
        snake.start()

    #gmap/ location command
    if having(query,['where is']):
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate"+location)

            webbrowser.open("https://www.google.co.in/maps/place/" + location)

    #opening application
    if having(query,['notepad']):
        speak("Opening notepad...")
        os.system("notepad")

    if having(query,['open code','vscode']):
        pCode="C:\\Users\\Ayush Panigrahi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening VS code...")
        os.startfile(pCode)

    if having(query,['whatsapp']):
        speak("opening whatsapp")
        wApp="C:\\Users\\Ayush Panigrahi\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(wApp)

    if having(query,['chrome, web browser']):
        web ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        speak(" opening chrome")
        os.startfile(web)

    if having(query,['excel','sheet']):
        eXcel="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
        speak("opening excel.")
        os.startfile(eXcel)

    '''if having(query, ['POWERPOINT','PPT']):
        speak("Opening MS Powerpoint...")
        os.system("powerpnt")
    if having(query, ['EXCEL','SHEETS']):
        speak("Opening MS excel...")
        os.system("excel")
    if having(query, ['cmd','command prompt','terminal']):
        speak("Opening prompt...")
        os.system("command prompt")'''

    if having(query,['calculate']):
        app_id = "Wolframalpha api id"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)


    # taking a photo
    if having(query,['shot','camera','snap']):
        speak("Stay still Capturing your beautiful face")
        ec.capture(0, "DXD camera ", "Assistant.jpg")

    """ DICTIONARY USE """

    '''if having(query,["what is the meaning of","what is the definition of","define"]):
        if "what is the meaning of" in query:
            query=query.replace('what is the meaning of ','')
        if "what is the definition of" in query:
            query = query.replace('what is the definition of ', '')
        if "define " in query:
            query=query.replace('define','')
        message(text=f"{query.capitalize()}: It is ..", bot=True)
        speak(f"{query}: It is ")
        word=PyDictionary()
        meaning=word.meaning(f"{query}")
        count=len(meaning['Noun'])
        if count>4:
            count=4
        for i in range(count):
            message(text=f"{meaning['Noun'][i]}", bot=True)
            speak(f"{meaning['Noun'][i]}")
        bot_status(False, False, True)'''

def bot_status(lsn=False,recgn=False,mic=False):
    if lsn:
        label.config(text="Listening...",fg="red",bg='black', font=("Helvetica", "16"))
        return
    if recgn:
        label.config(text="Recognizing...",fg="green",bg='black', font=("Helvetica", "16"))
        return
    if mic:
        label.config(text="",bg="white")
        return

def record():
    r=sr.Recognizer()
    with sr.Microphone() as mic:

        print("Listening")
        bot_status(True)
        uservoice=r.listen(mic)
        query=""
        try:
            print("Recognizing")
            bot_status(False,True)
            query=r.recognize_google(uservoice)
            message(text=f"{query}")
        except Exception as e:
            print(e)
            message(text="Could Not Hear You. Please Try Again",bot=True)
    return query.lower()

def runAssistant():
    query=record()
    if "thank you" in query:
        message(text="Your most welcome"+name,bot=True)
        speak("Your most welcome "+name+" will see you again")
        return
    else:
        command(query)
        label.configure(text="Tap the mic to speak", bg="black", fg="white", font=("Helvetica", "16"))
        label.pack()
        return

def message(text,bot=False):
    if bot:
        label.configure(text=f"{text}.", bg="black", wraplength=250, justify=LEFT,font=("Helvetica", "16"),fg='white')
    else:
        label.configure(text=text.capitalize(), wraplength=250, justify=LEFT, bg="black",font=("Helvetica", "16"),fg='white')

def animation(count):
    global anim
    label1.configure(image="")
    im2 = im[count]
    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    try:
        t1=Thread(target=runAssistant)
        t1.start()
    except Exception as e:
        print(e)
        if "you are offline" in e.lower():
            Label(text="You are Off line").pack()


gif_label = Label(root, image="", background="black")
gif_label.pack()

root.mainloop()
