import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=4 and hour<12:
        speak('Good Morning yusuf')
    elif hour>=12 and hour<=17:
        speak('good afternoon yusuf')
    elif hour>17 and hour<=20:
        speak('good evening yusuf')
    elif hour>20:
        speak('good night yusuf')
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('recognizing')
        query=r.recognize_google(audio,lauguage='en-in')
        print('user said ',query)
        return query
    except Exception as e:
        print('say that again please')
        return 'none'
if __name__=='__main__':
    wishme()
    while True:
        query=takecommand().lower()