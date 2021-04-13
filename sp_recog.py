import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something sir,")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
user_input = ""
input_list = []
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
        user_input = input = r.recognize_google(audio)
        # TEXT input("What is it sir?: ")
        # VOICE input = r.recognize_google(audio)
        input_list = user_input.split()
        print("Jarvis thinks you said " + user_input)
        if output == "text":
            return user_input
        if output == "list":
            return input_list
    read_input("What is it sir?: ", list)

except sr.UnknownValueError:
    print("Jarvis could not understand audio")
    activate("Say something sir,")
except sr.RequestError as e:
    print("Could not request results from Jarvis's recognition service; {0}".format(e))
    activate("Say something sir,")

