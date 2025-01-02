import os   # Imports the os module for interacting with the operating system
import pyautogui    # Imports the pyautogui module for automating keyboard and mouse actions
import webbrowser   # Imports the webbrowser module for opening web browsers
import pyttsx3  # Imports the pyttsx3 module for text-to-speech conversion
from time import sleep # Imports the sleep function from the time module for adding delays

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Defines a dictionary mapping common application names to their corresponding executable file names
dictapp = {"commondprompt":"cmd","paint":"paint","word":"word","window":"window","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}



# Defines a function to open applications or websites based on the user's query
def openappweb(query):
    speak("Initiating launch sequence, Luci.")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis", "")
        query = query.replace("launch","")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")



# Defines a function to close applications or tabs in web browsers based on the user's query
def closeaapweb(query):
    speak("Commencing shutdown protocol.")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("Lucifer, all tabs have been closed successfully.")

    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.2)
        pyautogui.hotkey("ctrl","w")
        speak("Lucifer, all tabs have been closed successfully.")

    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.2)
        pyautogui.hotkey("ctrl","w")
        sleep(0.2)
        pyautogui.hotkey("ctrl","w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        speak("Lucifer, all tabs have been closed successfully.")

    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        speak("Lucifer, all tabs have been closed successfully.")

    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.2)
        speak("Lucifer, all tabs have been closed successfully.")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")