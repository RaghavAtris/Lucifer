import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0

def Listen(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,0,5) # Listening Mode.....

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")
    except:
        return ""
    
    query = str(query).lower()
    return query

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data

def MicExecution(self):
    query = Listen(self)
    data = TranslationHinToEng(query)
    return data
