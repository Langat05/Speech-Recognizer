import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listening...")
        audio = r.listen(source)

    try:
        print("recognizing...")
        text = r.recognize_google(audio)  

    except:
        print("an error occured")
        return -1

    return str(text)   

print(listen())     
        
             