import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

# Function to speak the given text -----
def speak(audio):
    engine.say(audio)
    engine.runAndWait()   # Ensures that the speech is spoken synchronously

extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt", "r+")
datetime.truncate(0)
datetime.close()

def ring(time):
    time = str(time)
    timenow = timeset.replace("elio", "")
    timenow = timenow.replace("set an alarm", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing, Luci")
            os.startfile("music.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)