from voice import *
import datetime
from selenium_web import *
from YT_auto import *
from google_search import *
from open_sys_apps import *


def run_voice_assistant():
    marathi_mode = False
    speak_english("Hello sir, I am your voice assistant. How are you?")
    speak_english("Before continuing further, please tell me in which language you want me to speak to you? Marathi or English")
    text = listen_english()
    print(text)
    if text == "marathi":
        marathi_mode = True
    elif text == "english":
        marathi_mode = False
    else:
        speak_english("Sorry i didnt catch that or the language you're saying is might be not available so i am continuing in english")

    while True:
        if marathi_mode == False:
            speak_english("What can I do for you?")
        else:
            speak_marathi("मी तुमच्यासाठी काय करू शकते?")

        if marathi_mode == True:
            text2 = listen_marathi()
            print(text2)
        else:
            text2 = listen_english()
            print(text2)
        if text2:
            if any(word in text2 for word in ["change", "language", "भाषा बदल"]):
                marathi_mode = not marathi_mode  # Toggle the language mode

                if marathi_mode:
                    speak_marathi("ठीक आहे, आत्ता मी तुमच्याशी मराठीतून बोलणार आहे.")
                    speak_marathi("काही इतर करायचं आहे का?")
                else:
                    speak_english("OK, from now on I will talk to you in English.")
                    speak_english("Is there anything else you want me to do?")

            elif any(word in text2 for word in ["information", "माहिती", "wikipedia"]):
                # Handle commands in Marathi
                if marathi_mode == True:
                    print(speak_marathi("आपल्याला कुठल्या विषयाची माहिती पाहिजे?"))
                    infor = listen_english()
                    print(infor)
                    if infor:
                        speak_marathi("{} विकिपीडिया वर शोधत आहे".format(infor))
                        assist = infow()
                        assist.get_info(infor)
                        print(speak_marathi("इतर काही करायचं आहे का?"))
                    else:
                        print(speak_marathi("माफ करा मला समजले नाही, पुन्हा एकदा प्रयत्न करा "))
                elif marathi_mode == False:
                    speak_english("You need information related to which topic?")
                    infor = listen_english()
                    print(infor)
                    if infor:
                        speak_english("Searching {} on Wikipedia".format(infor))
                        assist = infow()
                        assist.get_info(infor)
                        speak_english("Is there anything else you want me to do?")
                    else:
                        speak_english("Sorry, I didn't understand. Can you please repeat?")
                # Add more Marathi commands here as needed
            elif any(word in text2 for word in ["play", "video", "youtube", "विडिओ", "प्ले", "यूट्यूब"]):
                # Handle commands in Marathi
                if marathi_mode == True:
                    speak_marathi("तुम्हाला कोणता व्हिडिओ प्ले करायचा आहे?")
                    vid = listen_english()
                    print(vid)
                    if vid:
                        speak_marathi("{} यूट्यूब वर प्ले होत आहे".format(vid))
                        assist = music()
                        assist.play(vid)
                        speak_marathi("इतर काही करायचं आहे का?")
                    else:
                        print(speak_marathi("माफ करा मला समजले नाही, पुन्हा एकदा प्रयत्न करा "))
                elif marathi_mode == False:
                    speak_english("You want me to play which video?")
                    vid = listen_english()
                    print(vid)
                    if vid:
                        speak_english("Playing {} on YouTube".format(vid))
                        assist = music()
                        assist.play(vid)
                        speak_english("Is there anything else you want me to do?")
                    else:
                        speak_english("Sorry, I didn't understand. Can you please repeat?")

            elif any(word in text2 for word in ["search", "शोध", "गूगल", "google"]):
                # Handle commands in Marathi
                if marathi_mode == True:
                    speak_marathi("आपल्याला गूगल वर काय शोधायचं आहे?")
                    goog = listen_english()
                    print(goog)
                    if goog:
                        speak_marathi(f"{goog} गूगल वर शोधित आहे.")
                        google_search(goog)
                        speak_marathi("इतर काही करायचं आहे का?")
                    else:
                        print(speak_marathi("माफ करा मला समजले नाही, पुन्हा एकदा प्रयत्न करा "))
                elif marathi_mode == False:
                    speak_english("What do you want to search on Google?")
                    goog = listen_english()
                    print(goog)
                    if goog:
                        speak_english(f"Searching {goog} on Google.")
                        google_search(goog)
                        speak_english("Is there anything else you want me to do?")
                    else:
                        speak_english("Sorry, I didn't understand. Can you please repeat?")

            elif any(word in text2 for word in ["time", "वेळ"]):
                # Handle commands in Marathi
                if marathi_mode == True:
                    now = datetime.datetime.now()
                    current_time = now.strftime("%I:%M %p")
                    current_date = now.date()
                    speak_marathi(f"सध्याची वेळ {current_time} आणि आजची तारीख {current_date} आहे.")
                    speak_marathi("इतर काही करायचं आहे का?")
                elif marathi_mode == False:
                    now = datetime.datetime.now()
                    current_time = now.strftime("%I:%M %p")
                    current_date = now.date()
                    speak_english(f"The current time is {current_time} and the today's date is {current_date}.")
                    speak_marathi("Is there anything else you want me to do?")

            elif any(word in text2 for word in ["open", "चालू", "app"]):
                # Handle commands in Marathi
                if marathi_mode == True:
                    speak_marathi("तुम्हाला काय चालू करायचे आहे?")
                    app = listen_english()
                    print(app)
                    if app:
                        open_apps(text2)
                        speak_marathi("इतर काही करायचं आहे का?")
                    else:
                        print(speak_marathi("माफ करा मला समजले नाही, पुन्हा एकदा प्रयत्न करा"))
                elif marathi_mode == False:
                        open_apps(text2)
                        speak_english("Is there anything else you want me to do?")

            elif any(word in text2 for word in ["quit", "exit", "close", "बंद"]):
                # Handle commands in Marathi
                if marathi_mode == True:
                    speak_marathi("ठीक आहे, मी बंद होते!")
                    break  # Exit the loop and terminate the program
                elif marathi_mode == False:
                    speak_english("Okay, goodbye!")
                    break  # Exit the loop and terminate the program

        else:
            if marathi_mode == True:
                speak_marathi("माफ करा मला समजले नाही, पुन्हा एकदा प्रयत्न करा")
            elif marathi_mode == False:
                speak_english("Sorry, I didn't catch that. Can you please repeat?")


if __name__ == "__main__":
    run_voice_assistant()