
# Import necessary libraries

import datetime  # For working with dates and times
import os
import pyautogui
import keyboard

import requests  # For making HTTP requests
import win32com.client  # For accessing Windows-specific functionalities
import speech_recognition  # For speech recokkgnition
import pyttsx3  # For text-to-speech conversion
import requests  # For making HTTP requestskk
from bs4 import BeautifulSoup  # For web scraping

# The code imports various libraries for different functionalities such as working with dates and times,
# making HTTP requests, accessing Windows-specific functionalities, speech recognition,
# text-to-speech conversion, and web scraping.



# This code initializes the pyttsx3 engine with the "sapi5" speech synthesis API,
# gets the available voices, sets the voice property to the first voice in the list of available voices,
# and sets the speech rate to 170 words per minute.
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


# Function to speak the given text -----
def speak(audio):
    engine.say(audio)
    engine.runAndWait()   # Ensures that the speech is spoken synchronously


# Function to recognize speech input ----
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Receiving auditory input...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("understanding your request...")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Could you please repeat that?")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")





if __name__ == "__main__":

    # This block of code executes when the script is run directly ---
    while True:
        query = takeCommand().lower()
        if "wake up" in query:      #start command "Wake Up"
            from GreetMe import greetMe
            greetMe()

            # Continuously listen for commands after waking up ---
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Alright, Lucifer, feel free to call on me anytime.")
                    break



    # Check for various conversation triggers and respond accordingly ---
                elif "hello" in query:
                    speak("Hello Lucifer, how are you ?")
                elif "nothig new" in query:
                    speak("oh! okay Luci")
                elif "how are you" in query:
                    speak("Perfect Luci")
                elif "thank you" in query:
                    speak("you are welcome, Luci")


                elif "who am " in query:
                    speak("Lucifer, you are a talented individual with expertise in web development and a passion for AI technology.")

                elif "who are you" in query:
                    speak("I was developed by you, Lucifer. You've created me to assist you with various tasks and to provide information whenever you need.")

                elif "good job " in query:
                    speak("Your gratitude is acknowledged, Luci.")


                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("vide muted")

                elif "volume up" in query:
                    from keyboard import  volumeup
                    speak("Increasing volume, Luci.")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Decreasing volume, Luci.")
                    volumedown()




    # Code for handling user requests to open and close apps ---

            # Check if the user wants to open an app --
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)

            # Check if the user wants to close an app ---
                elif "close" in query:
                    from Dictapp import closeaapweb
                    closeaapweb(query)




    # Code for handling user requests to search on Google, YouTube, and Wikipedia ---
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)




    # Code for retrieving current temperature and weather reports ---
                elif "temperature" in query:
                    search = "temperature in Kolkata"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"The current{search} is {temp}")

                elif "weather" in query:
                    search = "temperature in Kolkata"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"The current{search} is {temp}")

        # Code for retrieving and announcing the current time ---
                elif "current time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Luci, it's currently {strTime}.")

                elif "set an alarm" in query:
                    print("input time example: 10 and 10 and 10")
                    speak("Adjusting the time settings.")
                    a = input("Kindly provide the time: ")
                    alarm(a)
                    speak("Task completed, Luci.")



    # Code to initiate sleep mode and exit the program --
                elif "finally sleep" in query:   # the whole file will be closed
                    speak("Going to sleep")
                    exit()











