import pyttsx3 as p
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
import pygame
import time

# def speak_english(text):
#     engine = p.init()
#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', 180)
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.say(text)
#     engine.runAndWait()

def speak_english(text):
    engine = p.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    print("Speaking:", text)  # Print the text before speaking
    engine.say(text)
    engine.runAndWait()

# def speak_marathi(text):
#     try:
#         tts = gTTS(text=text, lang='mr')
#         audio_bytes = BytesIO()
#         tts.write_to_fp(audio_bytes)
#         audio_bytes.seek(0)
#
#         pygame.mixer.init()
#         pygame.mixer.music.load(audio_bytes)
#         pygame.mixer.music.play()
#
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#     except Exception as e:
#         print("Error:", e)


def speak_marathi(text):
    try:
        print("Speaking:", text)  # Print the text before speaking
        tts = gTTS(text=text, lang='mr')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        pygame.mixer.init()
        pygame.mixer.music.load(audio_bytes)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print("Error:", e)


def listen_english():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 20000
        r.adjust_for_ambient_noise(source, 1.5)
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en-US')  # Recognize English speech
        return text.lower()
    except sr.UnknownValueError:
        speak_english("Sorry, I didn't catch that. Can you please repeat?")
        return listen_english()
    except sr.RequestError:
        speak_marathi("Sorry, I'm having trouble accessing the Google API. Please try again later.")
        return None

def listen_marathi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 20000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="mr-IN")  # Recognize Marathi speech
        return text.lower()
    except sr.UnknownValueError:
        speak_marathi("माफ करा, मला समजलं नाही. कृपया पुन्हा करा?")
        return listen_marathi()
    except sr.RequestError:
        speak_marathi("माफ करा, मला Google API वर समस्या आहे. कृपया पुन्हा प्रयत्न करा.")
        return None

# if __name__ == "__main__":
#     # Example usage:
#     language = input("Enter language (en for English, mr for Marathi): ")
#     if language == 'en':
#         text = listen_english()
#         print("You said:", text)
#         speak_english(text)
#     else:
#         # text = listen_marathi()
#         while True:
#             text = input()
#             print("You said:", text)
#             speak_marathi(text)