import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Mustakim, I am your Voice Assistant within your system designed by you. Please tell me how may i help you.")

def takeCommand():
    #it take microphone input and return string input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I am Listening to Your voice")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("recognizing...")
        speak("Recognizing your speech")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")
        speak(f"You have asked for {query}")

    except Exception as e:
        print(e)
        print("Can you please say that again..")
        speak("Sorry! Your voice is not clear. Can you please say that again.")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mustakimmullick12345@gmail.com','Rajakulislam')
    server.sendmail('mustakimmullick12345@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

     #logic to execute command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia","") 
            results=wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak("Well Thank you! I am Great. Hoping to get some command from you.")

        elif 'bad' in query:
            speak("I am not designed to hear or say bad words to you, but if you say so.")

        elif 'open youtube' in query:
            speak("Opening Youtube on your system, Enjoy! But don't search bad stuff Ha-ha-ha-ha-ha-ha-ha.")
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            speak("Opening Instagram on your system, But don't waste your time there.")
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            speak("Opening Facebook on your system,But don't waste your time there.")
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            speak("Opening Google on your system, search safe!")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stack overflow on your system, Get your Solution and come back here.")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir= 'F:\\VIDEO SONGS\\English'
            songs= os.listdir(music_dir)
            speak("Opening Videos! Enjoy your Time. You can also sing along")
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
            speak("Use your time carefully! Be efficient.")

        elif 'open code' in query:
            speak("You want to code?, Good.")
            code_path="C:\\Users\\Mostakim Mullick\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(os.path.join(code_path))

        elif 'shut' in query:
            print("Shutting Voice Assistant")
            speak("As you have asked, i am shutting down myself! TAKE CARE!")
            exit()

        elif 'send email to Mustakim' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to ="mustakimmullick12345@gmail.com"
                sendEmail(to, content)
                speak("Email has benn send!")
            except Exception as e:
                print(e)
                speak("Some kind of error! It can't be send now.")
    

        
        

        

        