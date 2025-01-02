# Imports the pyttsx3 library for text-to-speech conversion
# Imports the datetime library for working with dates and times
import pyttsx3
import datetime


# Initializes the pyttsx3 engine with the "sapi5" speech synthesis API
# Retrieves the available voices and sets the voice property to the first voice
# Sets the speech rate to 170 words per minute
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)


# Defines a function to speak the provided audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Defines a function to greet the user based on the current time
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning, Lucifer. I'm Elio, your AI assistant.")
    elif hour >= 12 and hour<  18:
        speak("Good afternoon, Lucifer. I'm Elio, your AI assistant.")

    else:
        speak("Good evening, Lucifer. I'm Elio, your AI assistant.")

    speak("Please let me know how I can assist you.")