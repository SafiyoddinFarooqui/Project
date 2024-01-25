import pyttsx3
import datetime
import speech_recognition as sr
import random
import string
import wikipedia
import webbrowser
import pyautogui
from time import sleep
import smtplib
engine = pyttsx3.init()

def speak(txt):
    engine.say(txt)
    engine.runAndWait()
def wishme():
    hour=datetime.datetime.now().hour
    date=str(datetime.datetime.now().day)
    month=str(datetime.datetime.now().month)
    year=str(datetime.datetime.now().year)
    time=datetime.datetime.now().strftime("%H:%M:%S")
    print(date, month,year)
    X=hour
    print(time)
    if X>=0 and X<=6:
        print("Good Night")
        speak("Good Night")
    elif X>=6 and X<=12:
        speak("Good Morning")
        print("Good Morning")
    elif X >=12 and X<=18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")
    speak("The Current Date is")
    speak(date)
    speak(month)
    speak(year)
    speak("The Current Time is")
    speak(time)
    print("Jarvis at your service tell me how can I can help you?")
    speak("Jarvis at your service tell me how can I can help you?")
#wishme()


def Date():
    date=str(datetime.datetime.now().day)
    month=str(datetime.datetime.now().month)
    year=str(datetime.datetime.now().year)
    speak("The Current Date is")
    print(date,month,year)
    speak(date)
    speak(month)
    speak(year)



def time():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The Current Time is")
    print(time)
    speak(time)



def dice():
    dice=random.randrange(1,7)
    speak("Random Number is")
    print(dice)
    speak(dice)



def wiki():
    query=takecommandMIC()
    result=wikipedia.summary(query)
    speak("You searched")
    print(result)
    speak(result)
    

def web():
    url = 'https://www.google.com/search?q='
    speak("what should i sreach for?") 
    query=takecommandMIC()
    result1=webbrowser.open(url+query)
    speak(" opening on webbrowser")
    print(result1)
    speak(result1)
    
def password():
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    speak(" u random password is ")
    print("".join(s[0:8]))
    speak("".join(s[0:8]))


def sshot():
    sleep(5)
    ss= pyautogui.screenshot()
    ss.save("SS1.png")

def send_email(email,to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email,"jwsdlajoypwkchrn")
    # server.send_message()
    server.sendmail(email,to,content)
    server.close()
    

def takecommandCMD():
    query=input("Enter ur command\n")
    return query

def takecommandMIC():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...!")
        query=r.recognize_google(audio, language='en-in')
        print("user said:"+query)
    except Exception as e:
        print(e)
        speak("unable to recognize the audio")
        return "None"
    return query
while True:
    query = takecommandMIC().lower()
    #query=takecommandCMD().lower()
    print("User Input:"+query)
    if "date" in query:
        Date()
    elif "time" in query:
        time()   
    elif "wish me" in query:
        wishme()
    elif "random number" in query:
        dice()
    elif "wikipedia" in query:
        wiki()
    elif "search" in query:
        web()
    elif "random password" in query:
        password()
    elif "screenshot" in query:
        sshot()
    elif "email" in query:
        receiver={"A":"farooquisafiyoddin@gmail.com",
            "B":"khanasma6666@gmail.com"}
        speak("what should send?")
        content = takecommandMIC()
        send_email("spider9834man@gmail.com",receiver,content)
    elif "quit" in query:
        quit()
