import speech_recognition as sr
import pyttsx3
import webbrowser
engine = pyttsx3.init()
engine.runAndWait()
# log_file = open("log.txt", "r+")

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something sir,")
#     audio = r.listen(source)

# recognize speech using Google Speech Recognition
user_input = ""
input_list = []
command = ""
def first_president():
    engine.say("The first president is George Washington sir.")
    engine.runAndWait()
    return print("The first president is George Washington sir."), read_input("What is it sir?:", "list")

def repeat():
    phrase = input("What do you want me to say?: ")
    # VOICE sp_recog.read_input("What do you want me to say?: ", "text")
    # TEXT input("What do you want me to say?: ")
    engine.say(phrase)
    engine.runAndWait()
    return print(phrase), read_input("What is it sir?:", "list")

def new_tab():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('chrome://newtab')
    engine.say("I will open a new tab in google sir.")
    engine.runAndWait()
    return print("I will open a new tab in google sir."), read_input("What is it sir?:", "list")

def stop():
    engine.say("Ok, goodbye.")
    engine.runAndWait()
    print("Ok, goodbye")
    return

command = ""
def find_command():
    global command
    for word in input_list:
        if word == "Jarvis":
            index = input_list.index("Jarvis")+1
            while index < len(input_list):
                command = command + input_list[index] + " "
                index += 1
    return command
            
class Command:
    def __init__(self, name, keyword, phrase, function):
        self.name = name
        self.keyword = keyword
        self.phrase = phrase
        self.function = function

#Every word after "Jarvis" will turn into the phrase
    def respond(self):
        global command
        command = ""
        if find_command() == self.phrase + " ":
            if self.function == "first_president":
                first_president()
            if self.function == "repeat":
                repeat()
            if self.function == "new_tab":
                new_tab()
            if self.function == "stop":
                stop()

def dispatch():
    command1.respond()
    command2.respond()
    command3.respond()
    command4.respond()

command1 = Command("ask president", "Jarvis", "who is the first president", "first_president")
command2 = Command("repeat", "Jarvis", "repeat after me", "repeat")
command3 = Command("new tab", "Jarvis", "open a new tab", "new_tab")
command4 = Command("stop running", "Jarvis", "stop running", "stop")

try:
    # for testing purposes this is the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    def activate(ask):
        global r
        global audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(ask)
            audio = r.listen(source)
            read_input(ask, "text")

    def read_input(ask, output):
        global r
        global audio
        global user_input
        global input_list
        user_input = input(ask)
        # TEXT input(ask)
        # VOICE input = r.recognize_google(audio)
        input_list = user_input.split()
        print("Jarvis thinks you said " + user_input)
        if output == "text":
            return user_input, dispatch()
        if output == "list":
            return input_list, dispatch()
    read_input("What is it sir?: ", "list")

except sr.UnknownValueError:
    print("Jarvis could not understand audio")
    activate("Say something sir,")
except sr.RequestError as e:
    print("Could not request results from Jarvis's recognition service; {0}".format(e))
    activate("Say something sir,")




