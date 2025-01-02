import speech_recognition # Imports the speech_recognition library for speech recognition
import pyttsx3 # Imports the pyttsx3 library for text-to-speech conversion
import pywhatkit # Imports the pywhatkit library for performing various tasks using voice commands
import wikipedia # Imports the wikipedia library for accessing Wikipedia articles
import webbrowser # Imports the webbrowser module for opening web browsers


# Defines a function to capture and recognize speech input
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


query = takeCommand().lower()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Defines a function to search Google and retrieve information based on the query --
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google", "")
        speak("Here are the results I retrieved from Google.")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")


# Defines a function to search YouTube and play the requested video --
def searchYoutube(query):
    if "youtube" in query:
        speak("Here are the search results I found on YouTube!")
        query = query.replace("youtube search","")
        query = query.replace("youtube", "")
        query = query.replace("elio", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Luci")


# Defines a function to search Wikipedia and retrieve summarized information based on the query
def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Initiating search on Wikipedia...")
        query = query.replace("wikipedia","")
        query = query.replace("Jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("As per Wikipedia's information...")
        print(results)
        speak(results)






