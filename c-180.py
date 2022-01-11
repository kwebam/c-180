from tkinter import *
import speech_recognition as sr

root = Tk()
root.geometry("500x500")

def r_audio():
    speech_recongnisor = sr.Recognizer()
    with sr.Microphone as source:
        audio = speech_recongnisor.listen(source)
        voice_data = ''
    try:
        voice_data = speech_recongnisor.recongize_google(audio, language = 'en-in')
    except sr.UnknownValueError:
        print("Please repeat i did not get that")
    print(voice_data)
    
r_audio()
root.mainloop()