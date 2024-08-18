import pyttsx3 as p
import speech_recognition as sr
import datetime
from selenium_web import *
from YT_auto import *
from google_search import *
from open_sys_apps import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 20000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you please repeat?")
        return listen()
    except sr.RequestError:
        speak("Sorry, I'm having trouble accessing the Google API. Please try again later.")
        return None


def run_voice_assistant():
    marathi_mode = False
    speak("Hello sir, I am your voice assistant. How are you?")
    speak("Before continuing further, please tell me in which language you want me to speak to you?")
    text = listen()
    print(text)

    while True:
        speak("What can I do for you?")
        text2 = listen()
        print(text2)
        if text2:
            if "information" in text2:
                speak("You need information related to which topic?")
                infor = listen()
                print(infor)
                if infor:
                    speak("Searching {} on Wikipedia".format(infor))
                    assist = infow()
                    assist.get_info(infor)
                    speak("Is there anything else you want me to do?")
            elif all(word in text2 for word in ["play", "video"]):
                speak("You want me to play which video?")
                vid = listen()
                print(vid)
                if vid:
                    speak("Playing {} on YouTube".format(vid))
                    assist = music()
                    assist.play(vid)
                    speak("Is there anything else you want me to do?")
            elif "search" and "google" in text2:
                speak("What do you want to search on Google?")
                goog = listen()
                print(goog)
                speak(f"Searching {goog} on Google.")
                google_search(goog)
                speak("Is there anything else you want me to do?")
            elif "time" and "date" in text2:
                now = datetime.datetime.now()
                current_time = now.strftime("%I:%M %p")
                current_date = now.date()
                speak(f"The current time is {current_time} and the today's date is {current_date}.")
                speak("Is there anything else you want me to do?")
            elif "open" in text2:
                open_apps(text2)
                speak("Is there anything else you want me to do?")
            elif "quit" or "Exit" or "Close" in text2:
                speak("Okay, goodbye!")
                break  # Exit the loop and terminate the program
            else:
                speak("Sorry, I didn't understand. Can you please repeat?")

run_voice_assistant()



