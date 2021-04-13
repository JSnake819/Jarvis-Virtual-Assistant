import speech_recognition as sr
import commands
import pyttsx3
engine = pyttsx3.init()
engine.runAndWait()
from sp_recog import *
# log_file = open("log.txt", "r+")

command1 = commands.Command("ask president", "Jarvis", "who is the first president", "first_president")
command2 = commands.Command("repeat", "Jarvis", "repeat after me", "repeat")
command3 = commands.Command("new tab", "Jarvis", "open a new tab", "new_tab")

command3.respond()
command1.respond()
command2.respond()
