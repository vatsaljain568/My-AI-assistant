import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Alexa' in command:
                command = command.replace('Alexa', '')
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is" + time)
        print(time)
    elif 'information' in command:
        person = command.replace('information', '')
        info = wikipedia.summary(person)
        print(info)
        talk(info)
    # elif 'boyfriend' in command:
        # talk("Yes,I have a boyfriend his name is Vatsal jain and he is so cute")
    elif 'intelligent' in command:
        talk("Thank you all credit to myMr.Vatsal jain")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please say the command again")
        print("Please say the command again")


while True:
    run_alexa()
