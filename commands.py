import sp_recog
import pyttsx3
import webbrowser
engine = pyttsx3.init()
engine.runAndWait()
command = ""

for word in sp_recog.input_list:
    if word == "Jarvis":
        index = sp_recog.input_list.index("Jarvis")+1
        while index < len(sp_recog.input_list):
            command = command + sp_recog.input_list[index] + " "
            index += 1
            
class Command:
    def __init__(self, name, keyword, phrase, function):
        self.name = name
        self.keyword = keyword
        self.phrase = phrase
        self.function  = function

#Every word after "Jarvis" will turn into the phrase
    def respond(self):
        global command
        if command == self.phrase + " ":
            if self.function == "first_president":
                first_president()
            if self.function == "repeat":
                repeat()
            if self.function == "new_tab":
                new_tab()

def first_president():
    engine.say("The first president is George Washington sir.")
    engine.runAndWait()
    return print("The first president is George Washington sir.")

def repeat():
    phrase = sp_recog.activate("What do you want me to say?: ")
    # VOICE sp_recog.read_input("What do you want me to say?: ", "text")
    # TEXT input("What do you want me to say?: ")
    engine.say(phrase)
    engine.runAndWait()
    return print(phrase)

def new_tab():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('chrome://newtab')
    engine.say("I will open a new tab in google sir.")
    engine.runAndWait()
    return print("I will open a new tab in google sir.")